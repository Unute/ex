# time = {'0': 0}
#
# for s in open('222.txt'):
#     s = s.replace(';', ' ')
#     s = s.split()
#     time[s[0]] = int(s[1]) + max(time[k] for k in s[2:])
#
# print(max(time.values()))



# time = {'0': 0}
#
# for s in open('222.txt'):
#     s = s.replace(';', ' ')
#     s = s.split()
#     time[s[0]] = int(s[1]) + max(time[k] for k in s[2:])
#
# print(max(time.values()))
#
# m = -float('inf')
# for s in open('222.txt'):
#     s = s.split()
#     m = max(m, int(s[1]))
# print(m)


# time = {'0': 0}
#
# for s in open('222.txt'):
#     s = s.replace(';', ' ')
#     s = s.split()
#     time[s[0]] = int(s[1]) + max(time[k] for k in s[2:])
#
# print(max(time.values()))


# time = {'0': 0}
#
# for s in open('222.txt'):
#     s = s.replace(';', ' ')
#     s = s.split()
#     time[s[0]] = int(s[1]) + max(time[k] for k in s[2:])
#
# print(max(time.values()))



time = {'0': 0}

for s in open('222.txt'):
    s = s.replace(';', ' ')
    s= s.split()
    time[s[0]]= int(s[1]) + max(time[k] for k in s[2:])

print(max(time.values()))
