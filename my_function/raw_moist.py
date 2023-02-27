# Import the necessary library
from pyModbusTCP.client import ModbusClient
import time

class MOIST():
    # host = '192.168.200.100'
    # port = 502
    # # [Input,value,insert] detail input[address,data,index]_value[address,data,index]_insert[address,data,index]
    # modeF = [[400,125,20],[401,125,30],[402,125,40]]
    # modeV = [[403,125,50],[404,125,60],[405,125,70]]
    
    def __init__(self) -> None:
        self.host = '192.168.200.100'
        self.port = 502
        # [Input,value,insert] detail input[address,quantity,index]_value[address,quantity,index]_insert[address,quantity,index]
        self.modeF = [[400,10,0],[401,10,0],[402,10,0]]
        self.modeV = [[403,10,0],[404,10,0],[405,10,0]]
        
        self.client = ModbusClient(host='192.168.200.100', port=502)
        
        try:
            print('Opening client')
            self.client.open()
        except:
            print('offline')
            self.client.close()
            
    def mode_F_input (self):
        try:
            self.client.open()
            while True:
                F_input = self.client.read_holding_registers(self.modeF[0][0], self.modeF[0][1])
                index = int(self.modeF[0][2])
                print(f"Register 0: {F_input[index]}")
                time.sleep(2)
        except:
            print('Shutdown')
            
    def mode_F_value (self):
        try:
            self.client.open()
            while True:
                F_value = self.client.read_holding_registers(self.modeF[1][0], self.modeF[1][1])
                index = int(self.modeF[1][2])
                print(f"Register 0: {F_value[index]}")
                time.sleep(2)
        except:
            print('Shutdown')
            
    def mode_F_insert (self):
        try:
            self.client.open()
            while True:
                F_insert = self.client.read_holding_registers(self.modeF[2][0], self.modeF[2][1])
                index = int(self.modeF[2][3])
                print(f"Register 0: {F_insert[index]}")
                time.sleep(2)
        except:
            print('Shutdown')
            
    def mode_V_input (self):
        try:
            self.client.open()
            while True:
                V_input = self.client.read_holding_registers(self.modeV[0][0], self.modeV[0][1])
                index = int(self.modeV[0][3])
                print(f"Register 0: {V_input[index]}")
                time.sleep(2)
        except:
            print('Shutdown')
            
    def mode_V_value (self):
        try:
            self.client.open()
            while True:
                V_value = self.client.read_holding_registers(self.modeV[1][0], self.modeV[1][1])
                index = int(self.modeV[1][3])
                print(f"Register 0: {V_value[index]}")
                time.sleep(2)
        except:
            print('Shutdown')
            
    def mode_V_insert (self):
        try:
            self.client.open()
            while True:
                V_insert = self.client.read_holding_registers(self.modeV[2][0], self.modeV[2][1])
                index = index(self.modeV[2][3])
                print(f"Register 0: {V_insert[index]}")
                time.sleep(2)
        except:
            print('Shutdown')
        