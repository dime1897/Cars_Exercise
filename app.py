from flask import Flask, render_template, request
from flask_restful import Resource, Api
from wtforms import Form, IntegerField, StringField, validators, SubmitField, SelectField, FloatField, BooleanField
from cars import Cars
from uuid import UUID


app = Flask(__name__,
            static_url_path='/static', 
            static_folder='static')
dao=Cars()


api = Api(app)
basePath = '/api/v1'
car_fields=['make', 'model', 'cc', 'cv', 'engine', 'price', 'used']
engines = ['diesel', 'petrol', 'hybrid', 'electric']
infos_fields = ['UUID', 'user', 'car_details']
available_marks = ['']

class FilterForm(Form):
    mark_filter = SelectField('MARK', choices=available_marks)
    max_pot = IntegerField('CC MAX', [validators.number_range(700,8000)])
    max_price = FloatField('PREZZO MAX', [validators.number_range(0.1,1000000)])
    used = SelectField('TIPOLOGIA', choices=['', 'NUOVO', 'USATO'])
    submit = SubmitField('FILTRA')
class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

def validate_id(id:str) -> bool:
    try:  
        UUID(id)
        return True
    except: 
        return False

def validate_car_details(car_details:dict) -> bool:
    try:
        if len(car_details.keys()) != len(car_fields): 
            #Too much or not enough field
            return False
        for field in car_details.keys():
            if not field in car_fields:
                #Field non compliant
                return False
        #Field are correct, now check values
        if not isinstance(car_details['make'], str) or not isinstance(car_details['model'], str) or not isinstance(car_details['cc'], int) or not isinstance(car_details['cv'], int) or not car_details['engine'] in engines or not isinstance(car_details['price'], float) or not isinstance(car_details['used'], bool):
            return False
        if (len(car_details['make']) < 3) or (len(car_details['model']) < 3) or (car_details['cv'] < 59) or (car_details['cc'] < 0) or (car_details['price'] < 0):
            return False
        return True
    except:
        return False
    
def validare_user_stuct(infos:dict) -> bool:
    try:
        if not len(infos.keys()) == len(infos_fields): return False
        for field in infos.keys():
            if not field in infos_fields:
                return False
        if not validate_id(infos['UUID']) or not validate_car_details(infos['car_details']):
            return False
        if len(infos['user'].keys()) != 3:
            return False
        for field in infos['user'].keys():
            if not field in ['nome', 'cognome', 'email']:
                return False
        return True
    except: return False

class Cars_Management(Resource):
    def get(self, id):
        if not validate_id(id): return None, 404
        car_details = dao.get_car_details(id)
        if car_details is None: return None, 404
        else: return car_details, 200

    def post(self, id):
        if not validate_id(id): return None, 400
        car_details = request.json
        if not validate_car_details(car_details): return None, 400

        conflict = dao.get_car_details(id)
        if not conflict is None: return None, 409
        if not car_details['make'] in available_marks:
            available_marks.append(car_details['make'])
        dao.insert_car_details(id, car_details)
        return None, 201

class Clean_DB(Resource):
    def get(self):
        dao.clear_db()
        return None, 200   

class User_and_Cars(Resource):
    def post(self):
        input = request.json
        if not validare_user_stuct(input): return None, 400
        conflict = dao.get_car_details(input['UUID'])
        if not conflict is None:  return None, 409
        dao.insert_user(input)
        return None, 201

api.add_resource(Cars_Management, f'{basePath}/car/<id>')
api.add_resource(User_and_Cars, f'{basePath}/user/')
api.add_resource(Clean_DB, f'{basePath}/clean')

@app.route(f'{basePath}/list', methods=['GET', 'POST'])
def cars_list():
    cars_list = dao.get_cars_list()
    if request.method == 'GET':
        c={}
        cform = FilterForm(obj=Struct(**c))
        return render_template('cars_list.html', cars_list=cars_list, form=cform), 200
    if request.method == 'POST':
        cform = FilterForm(request.form)
        if cform.mark_filter.data != '':
            cars_list = [car for car in cars_list if car['make']==cform.mark_filter.data]
        if not cform.max_pot.data is None:
            cars_list = [car for car in cars_list if car['cc']<=cform.max_pot.data]
        if not cform.max_price.data is None:
            cars_list = [car for car in cars_list if car['price']<=cform.max_price.data]
        if cform.used.data == 'NUOVO':
            cars_list = [car for car in cars_list if car['used']==False]
        elif cform.used.data == 'USATO':
            cars_list = [car for car in cars_list if car['used']==True]
        
        return render_template('cars_list.html', cars_list=cars_list, form=cform), 200
        

if __name__ == '__main__':
    app.run()