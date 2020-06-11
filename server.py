import tkinter
import time
import os

curTime = ''
hour = tkinter.Label()
hour.pack()
needHour=(input("Input time which you need to shutdown your computer:"))

def tick():
    global curTime
    newTime = time.strftime('%H:%M:%S')
    if newTime != curTime:
        curTime = newTime
        hour.config(text=curTime)
    hour.after(200, tick)
    line=curTime
    if needHour in line:
        os.startfile(r'C:\shut.bat')

tick()
hour.mainloop()


'''
import time
import os
import psutil
b=float(input("Entered your threshold(%):"))
for proc in psutil.process_iter():
    p=psutil.Process(os.getpid())
    if(p.cpu_percent()<=b and ((p.cpu_times()[1])>0 and (p.cpu_times()[1])<0.1)):
        print("Name of Process:"+str(proc.name()))
        print("Status:"+str(p.status()))
        print("CPU%:"+str(p.cpu_percent())+"%")
        print("Time of system take:"+str((p.cpu_times()[1])))
        os.startfile(r'C:\shut.bat')
'''
'''
import socket
import os

so = socket.socket()
so.bind(('', 1000))
so.listen(1)
soed, at  = so.accept()

print ('connected:', at)
print('Entered your data:',end='')
Data=int(input())
while True:
    datas = soed.recv(1024)
    if at[1]<Data:
        os.startfile(r'C:\shut.bat')
        break
    elif not datas:
        break
    soed.send(datas)
soed.close()
'''