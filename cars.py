from google.cloud import firestore

class Cars(object):
    def __init__(self):
        self.db = firestore.Client(database='cars')

    def clear_db(self) -> None:
        cars_ref = self.db.collection('cars')
        users_ref = self.db.collection('users')
        try:
            for car in cars_ref.list_documents():
                car.delete()
            for user in users_ref.list_documents():
                user.delete()
        except Exception as e:
            print("Exception cought in clear_db():\n\n{" + str(e) + "}")

    def insert_car_details(self, id:str, car_details:dict) -> None:
        cars_ref = self.db.collection('cars')
        try:
            cars_ref.document(id).set(car_details)
        except Exception as e:
            print("Exception cought in insert_car_details():\n\n{" + str(e) + "}")

    def get_car_details(self, id:str) -> dict:
        cars_ref = self.db.collection('cars')
        try:
            doc = cars_ref.document(id).get()
            car_details = doc.to_dict() if doc.exists else None
            return car_details
        except Exception as e:
            print("Exception cought in get_car_details():\n\n{" + str(e) + "}")
            return None
        
    def insert_user(self, infos:dict) -> None:
        user_ref = self.db.collection('users')
        cars_ref = self.db.collection('cars')
        try:
            user_ref.document(infos['UUID']).set(infos['user'])
            cars_ref.document(infos['UUID']).set(infos['car_details'])
        except Exception as e:
            print("Exception cought in insert_user():\n\n{" + str(e) + "}")
            return None
        
    def get_cars_list(self) -> dict:
        cars_ref = self.db.collection('cars')
        try:
            doc_list = cars_ref.stream()
            ret_list = []
            for doc in doc_list:
                car = doc.to_dict()
                ret_list.append(car)
            return ret_list
        except Exception as e:
            print("Exception cought in get_cars_list():\n\n{" + str(e) + "}")
            return None