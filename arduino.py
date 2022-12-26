#pip install pyserial
#pip install machine
#python.exe -m pip install --upgrade pip
#pip install pycrypto
#pip install pip
#pip install wheel==0.24.0
#pip install micropython-upip
#pip install micropython-uctypes
#pip install pyFirmata
#pip install pyfirmata #Tino de Bruijn
#pip install pyserial pyqt5
#pip install PyQt5
#pip install PyQt5-tools
#pip install pyserial
#import machine
#from machine import Pin


import time
import pyfirmata

if __name__ == '__main__':
    board = pyfirmata.Arduino('COM3')
    board.digital[13].write(1)
    time.sleep(2)
    board.digital[13].write(0)
    time.sleep(2)
    print("Communication Successfully started")
    
    while True:
        board.digital[8].write(1)
        time.sleep(2)
        board.digital[8].write(0)
        time.sleep(1)


