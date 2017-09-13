'''
Created on 8 de set de 2017

@author: Lucas
'''

if __name__ == '__main__':
    pass

# import sys
import os


#p = os.popen('/usr/bin/zbarcam --nodisplay --raw /dev/video0', 'r')
p = os.popen('/usr/bin/zbarcam', 'r')

def start_scan():
    global p
    while True:
        print('Scanning')
        data = p.readline()
        qrcode = str(data)
        if(qrcode):
            print(qrcode)

try:
    start_scan()
except KeyboardInterrupt:
    print('Stop scanning')
finally:
    p.close()
