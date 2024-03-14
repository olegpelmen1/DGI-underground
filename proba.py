import struct

with open(name, "rb") as file:
     data = file.read()

ChunkID = data[0:4].decode()


fileSize = struct.unpack_from('i', data, offset=4)
print(fileSize)