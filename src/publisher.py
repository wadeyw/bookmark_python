import pika, os , logging
logging.basicConfig()

url=os.environ.get('CLOUDAMQP_URL',
                   'amqp://idosarnd:K1T59P-vGf6i8am6qRbi0ThMmQFHRZSE@rhino.rmq.cloudamqp.com/idosarnd')
params=pika.URLParameters(url)
params.socket_timeout=5
connection=pika.BlockingConnection(params)  # Connect to cloudamqp
channel=connection.channel()                # start a channel
channel.queue_declare(queue='testqueue')    # decalre a queue

channel.basic_publish(exchange='', routing_key='testqueue', body='User info') # send a message
print('[x] Message sent to consumer')

connection.close()