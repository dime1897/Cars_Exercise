import requests

url="http://localhost:8080/api/v1"

body = {
            'make': 'Alfa Romeo',
            'model': 'Giulia',
            'cc': 2200,
            'price': 25000.00,
            'engine': 'diesel',
            'cv': 160,
            'used': False
        }
#print("GET: "+url+"/clean")
#resp = requests.get(url+'/clean')
#print(str(resp) + ":" + resp.text)
#print('\n\n')

print("POST: "+url+"/car/0607273b-e8d0-46bb-8428-cda00298bf8c\nBODY: "+ str(body))
resp = requests.post(url+'/car/0607273b-e8d0-46bb-8428-cda00298bf8c', json= body)
print(str(resp) + ":" + resp.text)
print('\n\n')
#
#body = {
#            'make': 'Alfa Romeo',
#            'model': 'Giulietta',
#            'cc': 1800,
#            'price': 25000.00,
#            'engine': 'petrol',
#            'cv': 110,
#            'used': False
#        }
#print("POST: "+url+"/car/b6ae776d-7498-445d-b53d-fa08583a3b36\nBODY: "+ str(body))
#resp = requests.post(url+'/car/b6ae776d-7498-445d-b53d-fa08583a3b36', json= body)
#print(str(resp) + ":" + resp.text)
#print('\n\n')
#
#print("POST: "+url+"/car/d8ba26cd-32b1-4a52-bc87-4d2b40aca768\nBODY: "+ str(body))
#resp = requests.post(url+'/car/d8ba26cd-32b1-4a52-bc87-4d2b40aca768', json= body)
#print(str(resp) + ":" + resp.text)
#print('\n\n')
#
#body = {
#            'producer': 'Alfa Romeo',
#            'model': 'Giulietta',
#            'cc': 1800,
#            'price': 25000.00,
#            'engine': 'petrol',
#            'cv': 110,
#            'used': False
#        }
#
#print("POST: "+url+"/car/ff22636f-e004-4772-891d-0ed69d111574\nBODY: "+ str(body))
#resp = requests.post(url+'/car/ff22636f-e004-4772-891d-0ed69d111574', json=body)
#print(str(resp) + ":" + resp.text)
#print('\n\n')
#
#body = {
#            'make': 'Alfa Romeo',
#            'model': 'Giulietta',
#            'cilindrata': 1800,
#            'price': 25000.00,
#            'engine': 'petrol',
#            'cv': 110,
#            'used': False
#        }
#print("POST: "+url+"/car/ff22636f-e004-4772-891d-0ed69d111574\nBODY: "+ str(body))
#resp = requests.post(url+'/car/ff22636f-e004-4772-891d-0ed69d111574', json= body)
#print(str(resp) + ":" + resp.text)
#print('\n\n')
#
#body = {
#            'make': 'Alfa Romeo',
#            'model': 'Giulietta',
#            'cc': 1800,
#            'price': 25000.00,
#            'engine': 'hydrogen',
#            'cv': 110,
#            'used': False
#        }
#print("POST: "+url+"/car/ff22636f-e004-4772-891d-0ed69d111574\nBODY: "+ str(body))
#resp = requests.post(url+'/car/ff22636f-e004-4772-891d-0ed69d111574', json= body)
#print(str(resp) + ":" + resp.text)
#print('\n\n')
#
#body = {
#            'make': 'Fiat',
#            'model': '500X',
#            'cc': 1600,
#            'price': 28000.00,
#            'engine': 'hybrid',
#            'cv': 85,
#            'used': False
#        }
#print("POST: "+url+"/car/ff22636f-e004-4772-891d-0ed69d111574\nBODY: "+ str(body))
#resp = requests.post(url+'/car/ff22636f-e004-4772-891d-0ed69d111574', json= body)
#print(str(resp) + ":" + resp.text)
#print('\n\n')
#
#body = {
#            'make': 'Fiat',
#            'model': '500X',
#            'cc': -15,
#            'price': 28000.00,
#            'engine': 'hybrid',
#            'cv': 85,
#            'used': False
#        }
#print("POST: "+url+"/car/87c99007-ed03-46b6-a8c2-e52b403c9aa4\nBODY: "+ str(body))
#resp = requests.post(url+'/car/87c99007-ed03-46b6-a8c2-e52b403c9aa4', json= body)
#print(str(resp) + ":" + resp.text)
#print('\n\n')
#
#body = {
#            'make': 'Fiat',
#            'model': '500X',
#            'cc': 1555,
#            'price': 28000.00,
#            'engine': 'hybrid',
#            'cv': 10,
#            'used': False
#        }
#print("POST: "+url+"/car/87c99007-ed03-46b6-a8c2-e52b403c9aa4\nBODY: "+ str(body))
#resp = requests.post(url+'/car/87c99007-ed03-46b6-a8c2-e52b403c9aa4', json= body)
#print(str(resp) + ":" + resp.text)
#print('\n\n')
#
#body = {
#            'make': 'Fiat',
#            'model': '500X',
#            'cc': 1555,
#            'price': '28000.00',
#            'engine': 'hybrid',
#            'cv': 80,
#            'used': False
#        }
#print("POST: "+url+"/car/87c99007-ed03-46b6-a8c2-e52b403c9aa4\nBODY: "+ str(body))
#resp = requests.post(url+'/car/87c99007-ed03-46b6-a8c2-e52b403c9aa4', json= body)
#print(str(resp) + ":" + resp.text)
#print('\n\n')
#
#body = {
#            'make': 'Renault',
#            'model': 'Talisman',
#            'cc': 1800,
#            'price': 18000.00,
#            'engine': 'electric',
#            'cv': 95,
#            'used': True
#        }
#print("POST: "+url+"/car/87c99007-ed03-46b6-a8c2-e52b403c9aa4\nBODY: "+ str(body))
#resp = requests.post(url+'/car/87c99007-ed03-46b6-a8c2-e52b403c9aa4', json= body)
#print(str(resp) + ":" + resp.text)
#print('\n\n')

body = {
            'make': 'Renault',
            'model': 'Talisman',
            'cc': 1800,
            'price': 18000.00,
            'engine': 'electric',
            'cv': 95,
            'used': True
        }
print("POST: "+url+"/car/10555-632-5\nBODY: "+ str(body))
resp = requests.post(url+'/car/10555-632-5', json= body)
print(str(resp) + ":" + resp.text)
print('\n\n')

print("GET: "+url+"/car/b6ae776d-7498-445d-b53d-fa08583a3b36")
resp = requests.get(url+'/car/b6ae776d-7498-445d-b53d-fa08583a3b36')
print(str(resp) + ":" + resp.text)
print('\n\n')

print("GET: "+url+"/car/d8ba26cd-32b1-4a52-bc87-4d2b40aca768")
resp = requests.get(url+'/car/ff22636f-e004-4772-891d-0ed69d111574')
print(str(resp) + ":" + resp.text)
print('\n\n')

print("GET: "+url+"/car/87c99007-ed03-46b6-a8c2-e52b403c9aa4")
resp = requests.get(url+'/car/87c99007-ed03-46b6-a8c2-e52b403c9aa4')
print(str(resp) + ":" + resp.text)
print('\n\n')

print("GET: "+url+"/car/10555-632-5")
resp = requests.get(url+'/car/10555-632-5')
print(str(resp) + ":" + resp.text)
print('\n\n')

#body = {
#            'car_details': {'make': 'Alfa Romeo',
#            'model': 'Giulia',
#            'cc': 2200,
#            'price': 40000.00,
#            'engine': 'diesel',
#            'cv': 160,
#            'used': False},
#            'UUID': 'b6ae776d-7498-445d-b53d-fa08583a3b36',
#            'user': {
#                'nome': 'Diego',
#                'cognome': 'Mercoliano',
#                'email': 'miamail'
#            }
#        }
#print("GET: "+url+"/clean")
#resp = requests.get(url+'/clean')
#print(str(resp) + ":" + resp.text)
#print('\n\n')
#
#print("POST: "+url+"/user\nBODY: "+ str(body))
#resp = requests.post(url+'/user', json= body)
#print(str(resp) + ":" + resp.text)
#print('\n\n')
#
#
#body = {
#            'car_details': {'make': 'Alfa Romeo',
#            'model': 'Giulietta',
#            'cc': 1800,
#            'price': 25000.00,
#            'engine': 'petrol',
#            'cv': 110,
#            'used': False},
#            'UUID': 'd8ba26cd-32b1-4a52-bc87-4d2b40aca768',
#            'user':{
#                'nome': 'Sara',
#                'cognome': 'Ferrari',
#                'email': 'altramail'
#            }
#        }
#print("POST: "+url+"/user\nBODY: "+ str(body))
#resp = requests.post(url+'/user', json= body)
#print(str(resp) + ":" + resp.text)
#print('\n\n')
#
#body = {
#            'car_details': {'make': 'Fiat',
#            'model': 'Panda',
#            'cc': 1200,
#            'price': 4000.00,
#            'engine': 'petrol',
#            'cv': 65,
#            'used': True},
#            'UUID': 'ff22636f-e004-4772-891d-0ed69d111574',
#            'user':{
#                'nome': 'Filippo',
#                'cognome': 'Santucci',
#                'email': 'montalmail'
#            }
#        }
#print("POST: "+url+"/user\nBODY: "+ str(body))
#resp = requests.post(url+'/user', json= body)
#print(str(resp) + ":" + resp.text)
#print('\n\n')
#
#body = {
#            'car_details': {'make': 'Jaguar',
#            'model': 'XE-DIOCANE',
#            'cc': 2200,
#            'price': 15000.00,
#            'engine': 'diesel',
#            'cv': 170,
#            'used': True},
#            'UUID': '87c99007-ed03-46b6-a8c2-e52b403c9aa4',
#            'user':{
#                'nome': 'Roberto',
#                'cognome': 'Leonelli',
#                'email': 'suamail'
#            }
#        }
#print("POST: "+url+"/user\nBODY: "+ str(body))
#resp = requests.post(url+'/user', json= body)
#print(str(resp) + ":" + resp.text)
#print('\n\n')
#
#body = {
#            'car_details': {'make': 'Citroen',
#            'model': 'C3DIOCANE',
#            'cc': 1100,
#            'price': 20000.00,
#            'engine': 'hybrid',
#            'cv': 85,
#            'used': False},
#            'UUID': '0607273b-e8d0-46bb-8428-cda00298bf8c',
#            'user':{
#                'nome': 'Marco',
#                'cognome': 'Prapanzoni',
#                'email': 'mprapanzoni@mail.com'
#            }
#        }
#print("POST: "+url+"/user\nBODY: "+ str(body))
#resp = requests.post(url+'/user', json= body)
#print(str(resp) + ":" + resp.text)
#print('\n\n')
#
#body = {
#            'car_details': {'make': 'Ferrari',
#            'model': 'F420',
#            'cc': 3500,
#            'price': 575000.00,
#            'engine': 'electric',
#            'cv': 350,
#            'used': False},
#            'UUID': '2b2174b5-1387-41eb-bd2b-5758f5c4df34',
#            'user':{
#                'nome': 'Alessandro',
#                'cognome': 'De Luca',
#                'email': 'alemaildioca'
#            }
#        }
#print("POST: "+url+"/user\nBODY: "+ str(body))
#resp = requests.post(url+'/user', json= body)
#print(str(resp) + ":" + resp.text)
#print('\n\n')