from dynamixel_sdk import *
ADDR_ID = 3  # Address for ID in the control table
PROTOCOL_VERSION = 1.0  # Use 1.0 for AX-12A
BAUDRATE = 1000000  # Default baudrate for AX-12A
DEVICENAME = '/dev/ttyACM0'  # Adjust this to your port name
portHandler = PortHandler(DEVICENAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    quit()
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    quit()
current_id = 12  # Replace with the current ID of your servo
new_id = 1  # Replace with the desired new ID

dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, current_id, ADDR_ID, new_id)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Servo ID successfully changed from", current_id, "to", new_id)
portHandler.closePort()
