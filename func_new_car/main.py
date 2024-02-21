from google.cloud import firestore
from google.cloud import pubsub_v1

db = firestore.Client(database='cars')
PROJECT_ID = 'exercises-00'
publisher = pubsub_v1.PublisherClient()

def create_topic(car:dict) -> None:
    topic = publisher.create_topic(request={
        "name": publisher.topic_path(PROJECT_ID, "make"+car['make']+"-model"+car['model']+"-engine"+car['engine']+"-cc"+str(car['cc'])+"-cv"+str(car['cv'])+"-used"+str(car['used']))
    })

    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(PROJECT_ID, "make"+car['make']+"-model"+car['model']+"-engine"+car['engine']+"-cc"+str(car['cc'])+"-cv"+str(car['cv'])+"-used"+str(car['used']))

    with subscriber:
        subscription = subscriber.create_subscription(request={
            "name": subscription_path, 
            "topic": publisher.topic_path(PROJECT_ID, "make"+car['make']+"-model"+car['model']+"-engine"+car['engine']+"-cc"+str(car['cc'])+"-cv"+str(car['cv'])+"-used"+str(car['used']))
        })

    print(f'Created topic: {topic.name}')

def check_new_car(data, context):
    cars_ref = db.collection('cars')
    cars_list = [car.to_dict() for car in cars_ref.stream()]
    found=False
    for car in cars_list:
        if car['make']==str(data['value']['fields']['make']['stringValue']) and car['model']==str(data['value']['fields']['model']['stringValue']) and car['used']==bool(data['value']['fields']['used']['booleanValue']) and car['cc']==int(data['value']['fields']['cc']['integerValue']) and car['cv']==int(data['value']['fields']['cv']['integerValue']) and car['price']>float(data['value']['fields']['price']['doubleValue']) and car['engine']==str(data['value']['fields']['engine']['stringValue']):
            found = True
            topic_path = publisher.topic_path(PROJECT_ID, "make"+(car['make'].replace(" ", ""))+"-model"+(car['model'].replace(" ", ""))+"-engine"+car['engine']+"-cc"+str(car['cc'])+"-cv"+str(car['cv'])+"-used"+str(car['used']))
            publisher.publish(topic_path, 'less price detected'.encode('utf-8')).result()

    if not found:
        car = {
            'make': data['value']['fields']['make']['stringValue'].replace(" ", ""),
            'model': data['value']['fields']['model']['stringValue'].replace(" ", ""),
            'cc': data['value']['fields']['cc']['integerValue'],
            'cv': data['value']['fields']['cv']['integerValue'],
            'engine': data['value']['fields']['engine']['stringValue'].replace(" ", ""),
            'used': data['value']['fields']['used']['booleanValue'],
            'price': data['value']['fields']['price']['doubleValue']
        }
        create_topic(car)
    