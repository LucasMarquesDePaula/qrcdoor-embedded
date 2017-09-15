'''
Created on 8 de set de 2017

@author: Lucas
'''
import os

p = os.popen('/usr/bin/zbarcam --nodisplay --raw /dev/video0', 'r')

def scan(on_start, on_scan):
    global p
    while True:
        if(on_start):
            on_start()
            
        data = p.readline()
        qrcode = str(data)
        if(qrcode):
            if(on_scan):
                on_scan(qrcode)

def run(args):
    try:
        scan(args.on_start, args.on_scan)
    except KeyboardInterrupt:
        print('Stop scanning')
        if(args.on_error):
            args.on_error()
    finally:
        p.close()
        if (args.on_stop):
            args.on_stop()
