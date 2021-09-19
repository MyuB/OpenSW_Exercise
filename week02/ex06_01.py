#이거 뭔가 이상하다


f = open('test.txt', 'a')
text = "Engine vibrations can harm phones'\nOptical image stabilisation or close-loop autofocus systems, it says.\nOwners of scooters and mopeds should also use biration-dampening mounts\n"
f.write(text)
f.close()

f = open('test.txt', 'r')
f_copy = open('test_copy.txt', 'w')
while True:
    line = f.readline().strip()
    if not line: break
    f_copy.write(line)

f_copy.close()
f.close()




