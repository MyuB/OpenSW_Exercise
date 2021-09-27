#이거 뭔가 이상하다

f = open('test.txt', 'a')
text = "Engine vibrations can harm phones'\nOptical image stabilisation or close-loop autofocus systems, it says.\nOwners of scooters and mopeds should also use biration-dampening mounts\n"
f.write(text)
f.close()

f = open('test.txt', 'r')
f_copy = open('test_copy.txt', 'w')
while True:
    line = f.readline()
    if not line: break
    f_copy.write(line)

f_copy.close()
f.close()

'''
아 이거 의도가 뭔지 몰라서 strip을 해버렸었음
fa = open("test.txt", 'a')
a = "Engine vibrations can harm phones'\nOptical-image stabilisation or closed-loop autofocus systems, it says.\nOwners of scooters and mopeds should also use vibration-dampening mounts\n"
fa.write(a)
fa.close()

fr = open("test.txt", 'r')
fw = open("test_copy.txt", 'w')

while True:
    line = fr.readline()
    if not line: break
    fw.write(line)

fw.close()
fr.close()
'''