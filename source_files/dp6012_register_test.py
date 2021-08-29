# lines used to explore DP registers

import minimalmodbus
 
instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1) # port name, slave address (in decimal)
instrument.serial.port          # this is the serial port name
instrument.serial.baudrate = 115200   # Baud rate used. see setting in DP unit
instrument.serial.bytesize = 8
instrument.serial.timeout = 0.5     # common used
 
 
instrument.mode = minimalmodbus.MODE_RTU  #RTU mode 
 

#instrument.write_register(8,11)
#instrument.write_register(9,300)

dump = instrument.read_registers(0x00,20)
print (dump)

# for i in range(129):
#     output = instrument.read_register(i, 0)   #read registers 0x0 to 0x80
#     #print(hex(i)[2:].zfill(2), output)
#     print (output)
