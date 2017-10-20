'''
Created on 8 de set de 2017

@author: Lucas
'''
import os
from threading import Thread

class QRCScanner(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        try:
#            p = os.popen('/usr/bin/zbarcam --nodisplay --raw /dev/video0', 'r')
            p = os.popen('/usr/bin/zbarcam /dev/video0', 'r')
            while True:
                self.on_scan(p.readline())
        except KeyboardInterrupt as e:
#        That's normal
            self.stop()
        except Exception as e:
            self.on_error(e)
        finally:
            p.close()
            self.on_stop()

    def on_scan(self, qrcode):
        print('INFO: QR code has been aquired: {0}'.format(qrcode))

    def on_stop(self):
        print('INFO: QR code scanner has been stopped')

    def on_error(self, error):
        print('ERROR: QR code scanner error has been occurred')
        print(error)
