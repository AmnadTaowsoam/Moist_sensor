import time
running = True
secounds = 0
end = 10
while (running):
    print(secounds)
    time.sleep(1)
    secounds +=1
    if (secounds >= end):
        running = False
        print('y')
print('Done')



###########################
from pyModbusTCP.client import ModbusClient
import time
import pandas as pd

# [Input,value,insert] detail input[address,quantity,index]_value[address,quantity,index]_insert[address,quantity,index]
modeF = [[400,10,0],[401,10,0],[402,10,0]]
modeV = [[403,10,0],[404,10,0],[405,10,0]]

client = ModbusClient(host='192.168.200.100', port=502)
client.open()
sensor_input = []

running = True
secounds = 0
end = 10
    
while (running):
    sensor_data = client.read_holding_registers(400,10)
    input = float(sensor_data[0])
    print(f"Register 0: {input}")
    sensor_input.append(input)
    print(secounds)
    time.sleep(1)
    secounds +=1
    if (secounds >= end):
        running = False
        print('y')
sensor_input

#####################################
import pandas as pd
import time
import os
import datetime
from matplotlib import pyplot as plt
import seaborn as sns

def plot_data(df): #plot data
    plt.figure(figsize=(15,8))
    ax = sns.lineplot(x="sampling", y="F_input(mA)", data=df)

#raw_data = [110,112,113,114,115,116,117,118,119,120,110,111,112,113,114,115]

def data_to_excel(raw_data):
    data = []
    for i in range(len(raw_data)):
        input = [i+1,raw_data[i]]
        data.append(input)
        print (data)
        time.sleep(1)
    df = pd.DataFrame(data, columns=['sampling','F_input(mA)'])
    df[['insert(k)','Value(Moist_reading)','Value(Moist_act)']]=""
    rootDir = './data_export/'
    filename = f"Calibrate_{datetime.datetime.now().strftime('%Y%m%d')}"
    plot_data(df)
    df.to_excel(rootDir + filename + '.xlsx')


raw_data = [110,112,113,114,115,116,117,118,119,120,110,111,112,113,114,115]
data_to_excel(raw_data)