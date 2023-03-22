import os
from int8 import int8

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

# ok time to execution!!!11!

code = byte_pairs
print("nlpc-1old emulator")

dinst = {
    "cjnz": 127,
    "cmov": 112,
    "cimm": 119,
    "calc": 122
}

regs = {
    "imm": int8(0),
    "x": int8(0),
    "y": int8(0),
    "acc": int8(0),
    "bus0": int8(0),
    "bus1": int8(0)
}
regnums = {
    0: "imm",
    1: "x",
    2: "y",
    3: "acc",
    4: "bus0",
    5: "bus1"
}

calcmodes = {
    0: (lambda x, y: x + y),
    1: (lambda x, y: x - y),
    2: (lambda x, y: x * y),
    3: (lambda x, y: x // y),
    
    4: (lambda x, y: x & y),
    5: (lambda x, y: x | y),
    6: (lambda x, y: ~x & y),
    7: (lambda x, y: x ^ y),
}

print("starting emulation")
pointer = 0

while pointer < len(code):
    ins = code[pointer]
    opcode = int(ins[0])
    data = int8(ins[1])
    inc = True
    if opcode == dinst["cjnz"]:
        print("%d: cjnz %s" % (pointer, data))
        if regs["acc"] != 0:
            pointer = data*2
            inc = False
    elif opcode == dinst["cmov"]:
        print("%d: cmov %s" % (pointer, data))
        movreg0 = int(data & int8(0x0F))
        movreg1 = int((data & int8(0xF0)) / int(16))
        regs[regnums[movreg1]] = regs[regnums[movreg0]]
    elif opcode == dinst["cimm"]:
        print("%d: cimm %s" % (pointer, data))
        regs["imm"] = data
    if inc:
        pointer += 1
