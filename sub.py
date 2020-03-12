import paho.mqtt.client as mqtt
from helper import *

f = open('pub.pem','r',encoding='utf-8')
pub=f.read()
pubkey=load_pub_key(pub)



broker_url = "broker.hivemq.com"
broker_port = 1883

def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code: {}".format(rc))

def on_disconnect(client, userdata, rc):
    print("Client Got Disconnected")

def on_message(client, userdata, message):
    text = message.payload.decode("utf-8")
    arr = text.split("#");
    cmd = arr[0]
    ts = arr[1]
    sign_hex = arr[2]
    text = "{}#{}".format(cmd,ts)
    if(verify(text,sign_hex,pubkey)):
        print(cmd)
    else:
        print("auth err")
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_url, broker_port)
client.subscribe("/message/from/me", qos=1)
client.loop_forever()
