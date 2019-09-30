flag = ""

with open("tinyelf", "rb") as elf:
    data = elf.read()
    total = (sum(data[0:96])-1) & 0xff

    for i in range(32):
        total = (total + data[96+i]) & 0xff
        flag = chr(total ^ 0xdb) + flag

print(flag)