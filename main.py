import os

inputfile = None
while inputfile is None or not os.path.exists(inputfile):
    inputfile = input("Enter a valid file path: ")

byte_list = []
byte_pairs = []

with open(inputfile, "rb") as f:
    byte = f.read(1)
    while byte:
        byte_list.append(ord(byte))
        byte = f.read(1)
if len(byte_list) % 2 != 0:
    byte_list.pop()  # whoopsies, overflow :(
for i in range(0, len(byte_list), 2):
    byte_pairs.append((byte_list[i], byte_list[i+1]))


print(byte_pairs)