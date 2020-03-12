import paho.mqtt.client as mqtt
from helper import *
import sys

broker_url = "broker.hivemq.com"
broker_port = 1883

client = mqtt.Client()
client.connect(broker_url, broker_port)

f = open('pri.pem','r',encoding='utf-8')
pri=f.read()
prikey=load_pri_key(pri)

cmd=sys.argv[1]

ts = get_time()
text = "{}#{}".format(cmd,ts)
sign_hex=sign(text,prikey)
payload = "{}#{}".format(text,sign_hex)
client.publish(topic="/message/from/me", payload=payload, qos=1, retain=False)
