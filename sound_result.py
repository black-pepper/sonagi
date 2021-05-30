import time
check = 0
while check == 0:
    try:
        f = open('recognition.txt', 'r')
        line = int(f.readline())
        # print(line)
        f.close()

        if line%100000 < 10000:
            line = line + 10000

        f = open('recognition.txt', 'w')
        f.write(str(line))
        f.close()

        check = 1
    except:
        continue

time.sleep(2)
check = 0
while check == 0:
    try:
        f = open('recognition.txt', 'r')
        line = int(f.readline())
            # print(line)
            f.close()

            if line%100000 >= 10000:
                line = line - 10000

            f = open('recognition.txt', 'w')
            f.write(str(line))
            f.close()

            check = 1
        except:
            continue
