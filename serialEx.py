import serial
import io
import matplotlib.pyplot as plt
import re

def main(lstTemp, lstLux, lstDist, tempThr, Port):
    temp = 0
    lux = 0
    prec = 0
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = Port
    ser.open()
    f1 = plt.figure(num="Temperatura")
    ax1 = f1.add_subplot(111)
    plt.xlabel("Tiempo")
    plt.ylabel("Grados",)
    while True:
        mem = ser.readline()
        tagged = re.findall(r'[TLP]', str(mem))
        tag = tagged[0]
        sersort = re.findall(r'[TLP]\d\d\d{1,2}', str(mem))
        sorteado = sersort[0]
        if tag == 'T':
            pretemp = re.findall(r'\d{1,4}', str(mem))
            temp = int(pretemp[0])
            tempReal = temp*5/255*100
            lstTemp.append(tempReal)
            if (tempReal) > tempThr:
                ser.write(str.encode('3'))
            else:
                ser.write(str.encode('6'))
        elif tag == 'L':
            prelux = re.findall(r'\d{1,4}', str(mem))
            lux = int(prelux[0])
            lstLux.append(lux*5/255)
        else:
            preprec = re.findall(r'\d{1,4}', str(mem))
            prec = int(preprec[0])
            lstDist.append(prec*5/255)
        ax1.plot(lstTemp,'-o', color = 'r',label = 'Temp')
        ax1.plot(lstLux,'-o', color = 'g',label = 'Luz')
        ax1.plot(lstDist,'-o', color = 'b',label = 'Distancia')
        plt.pause(0.5)
        plt.legend
        plt.show
    ser.close()

if __name__ == '__main__':
    tempThr = 27
    Port = 'COM4'
    lstTemp = []
    lstLux = []
    lstDist = []
    main(lstTemp, lstLux, lstDist, Port)
