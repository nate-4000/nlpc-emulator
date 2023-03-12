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

# ok time to execution!!!11!

def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val 

code = byte_pairs
version = input("nlpc version (nlpc-1, nlpc-1old, nlpc-2):")
if version == "nlpc-1":
    bus = True
elif version == "nlpc-1old":
    bus = False
else:
    bus = "nlpc-2"

dinst = {
    "cjnz": 127,
    "cmov": 112,
    "cimm": 119
}

regs = {
    "imm": 0,
    "x": 0,
    "y": 0,
    "acc": 0,
    "bus0": 0,
    "bus1": 0
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
    0: (lambda x, y: (x + y) & 0xFF),
    1: (lambda x, y: (x - y) & 0xFF),
    2: (lambda x, y: (x * y) & 0xFF),
    3: (lambda x, y: (x // y) & 0xFF),
    
    4: (lambda x, y: (x & y) & 0xFF),
    5: (lambda x, y: (x | y) & 0xFF),
    6: (lambda x, y: ~(x & y) & 0xFF),
    7: (lambda x, y: (x ^ y) & 0xFF),
}

print("starting emulation")
pointer = 0

while pointer < len(code):
    ins = code[pointer]
    opcode = ins[0]
    data = ins[1] & 0xFF
    inc = True
    if opcode == dinst["cjnz"]:
        print("%d: cjnz %s" % (pointer, data))
        if regs["acc"] != 0:
            pointer = data*2
            inc = False
    elif opcode == dinst["cmov"]:
        print("%d: cmov %s" % (pointer, data))
        movreg0 = data & 0x0F
        movreg1 = (data & 0xF0) / 16
        regs[regnums[movreg1]] = regs[regnums[movreg0]]
    elif opcode == dinst["cimm"]:
        print("%d: cimm %s" % (pointer, data))
        regs["imm"] = data & 0xFF
    if inc:
        pointer += 1
