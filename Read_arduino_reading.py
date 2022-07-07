import serial
import pyautogui

Arduino = serial.Serial('COM4', 9600)

while True:
    
    if Arduino.inWaiting() > 0:
        data = Arduino.readline().decode('ascii') 
        print(data)
        print(type(data))
        if int(data) == 1:
            pyautogui.press('space')

