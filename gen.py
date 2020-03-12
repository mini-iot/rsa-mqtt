from helper import *
pub,pri = gen_pem()

f = open('pub.pem', 'w')
f.write(pub)

f = open('pri.pem', 'w')
f.write(pri)
