import os

inputfile = None
while inputfile is None or not os.path.exists(inputfile):
    inputfile = input("Enter a valid file path: ")

byte_list = []

with open(inputfile, "rb") as f:
    byte = f.read(1)
    while byte:
        byte_list.append(ord(byte))
        byte = f.read(1)

print(byte_list)