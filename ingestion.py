from google.cloud import pubsub_v1

PROJECT_ID = 'exercises-00'


def callback(message):
    message.ack()
    msg = message.data.decode('utf-8')
    print(msg)

if __name__=='__main__':
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(PROJECT_ID, "makeAlfaRomeo-modelGiulia-enginediesel-cc2200-cv160-usedFalse")
    pull = subscriber.subscribe(subscription_path, callback=callback)
    try:
        pull.result()
    except Exception as e:
        print(e)
        pull.cancel()
