#  test lines to explore posibilities registers DP6012

import minimalmodbus
import datetime  
 
instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1) # port name, slave address (in decimal)
instrument.serial.port          # this is the serial port name
instrument.serial.baudrate = 115200   # Baud rate used. see setting in DP unit
instrument.serial.bytesize = 8
instrument.serial.timeout = 0.5     # common used
instrument.mode = minimalmodbus.MODE_RTU  #RTU mode 


  
  
# synchronize time  PC ==> DP6012
  
time = datetime.datetime.now()
  
print("Year: ", time.timetuple()[0])
print("Month: ", time.timetuple()[1])
print("Day: ", time.timetuple()[2])
print("Hour: ", time.timetuple()[3])
print("Minute: ", time.timetuple()[4])
print("Second: ", time.timetuple()[5])
print("Day of Week: ", time.timetuple()[6])
print("Day of Year: ", time.timetuple()[7])
print("Daylight Saving Time: ", time.timetuple()[8])
  
instrument.write_register(0x30,time.timetuple()[0])
instrument.write_register(0x31,time.timetuple()[1])
instrument.write_register(0x32,time.timetuple()[2])
instrument.write_register(0x33,time.timetuple()[3])
instrument.write_register(0x34,time.timetuple()[4])
instrument.write_register(0x35,(time.timetuple()[5])+1)  # compensate 1 second for write delay

#instrument.write_register(8,11)
#instrument.write_register(9,300)

dump = instrument.read_registers(0x00,60)
print (dump)

# for i in range(129):
#     output = instrument.read_register(i, 0)   #read registers 0x0 to 0x80
#     #print(hex(i)[2:].zfill(2), output)
#     print (output)

