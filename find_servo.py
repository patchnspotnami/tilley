import os
from dynamixel_sdk import *

# Protocol version
PROTOCOL_VERSION            = 1.0

# Default setting
DXL_ID                      = 1     # Dynamixel ID : 1
BAUDRATE                    = 1000000
DEVICENAME                  = '/dev/ttyACM0'  # Check which port is being used on your controller

# Control table address
ADDR_AX_ID                  = 3

# Open port
portHandler = PortHandler(DEVICENAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)

if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    quit()

# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    quit()

# Try to ping the Dynamixel
for id in range(0, 253):  # possible ID range
    dxl_model_number, dxl_comm_result, dxl_error = packetHandler.ping(portHandler, id)
    if dxl_comm_result != COMM_SUCCESS:
        continue
    print("[ID:%03d] ping Succeeded. Dynamixel model number : %d" % (id, dxl_model_number))

# Close port
portHandler.closePort()
