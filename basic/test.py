import requests
import json
import xlrd
import time
import weakref

def bye():
    print('bye bye')
S1= {1,2}
S2 = S1
tf = weakref.finalize(S1, bye)
del S1
S2 ={4,3}
TF = tf.alive
print(TF)