# ip1 = [bin(int(x))[2:].zfill(8) for x in '70'.split('.')]
# ip2 = [bin(int(x))[2:].zfill(8) for x in '107'.split('.')]
# print(*ip1)
# print(int('01000000', 2))
# print(*ip2)

# ip1 = [bin(int(x))[2:].zfill(8) for x in '201.92.0.20'.split('.')]
# ip2 = [bin(int(x))[2:].zfill(8) for x in '201.92.0.49'.split('.')]
# print(*ip1)
# print(int('11000000', 2))
# print(*ip2)

# ip1 = [bin(int(x))[2:].zfill(8) for x in '203.75.227.102'.split('.')]
# ip2 = [bin(int(x))[2:].zfill(8) for x in '203.75.224.0'.split('.')]
# print(*ip1)
# print(int('11111100', 2))
# print(*ip2)


ip1 = [bin(int(x))[2:].zfill(8) for x in '140.28'.split('.')]
ip2 = [bin(int(x))[2:].zfill(8) for x in '140.0'.split('.')]
print(*ip1)
print()
print(*ip2)







