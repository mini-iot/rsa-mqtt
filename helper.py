# -*- coding:utf-8 -*-
import rsa
from hashlib import md5
import time, datetime
def gen_pem():
    public_key, private_key = rsa.newkeys(512)
    pub = public_key.save_pkcs1()
    pri = private_key.save_pkcs1()
    pub_str = str(pub, encoding="utf-8")
    pri_str = str(pri, encoding="utf-8")
    return pub_str,pri_str

def load_pub_key(pub_str):
    b = pub_str.encode(encoding='utf-8')
    return rsa.PublicKey.load_pkcs1(b)

def load_pri_key(pri_str):
    b = pri_str.encode(encoding='utf-8')
    return rsa.PrivateKey.load_pkcs1(b)

def hash(text):
    m=md5()
    m.update(text.encode(encoding='utf-8'))
    hashstr=m.hexdigest()
    return hashstr

def sign(text,private_key):
    hashstr=hash(text)
    sign_b=rsa.sign(hashstr.encode(encoding='utf-8'), private_key, 'MD5')
    sign_hex = bytesToHexString(sign_b)
    return sign_hex

def verify(text,sign_hex,public_key):
    sign_b = hexStringTobytes(sign_hex)
    hashstr=hash(text)
    try:
        rsa.verify(hashstr.encode(encoding='utf-8'), sign_b, public_key)
        return True
    except:
        return False

def encrypt(text, public_key):
    msg = text.encode('utf8')
    return rsa.encrypt(msg, public_key)

def decrypt(crypto,private_key):
    msg = rsa.decrypt(crypto, private_key)
    text = msg.decode('utf8')
    return text

def get_time():
    return datetime.datetime.now()

def bytesToHexString(bs):
    return ''.join(['%02X ' % b for b in bs])

def hexStringTobytes(str):
    str = str.replace(" ", "")
    return bytes.fromhex(str)
