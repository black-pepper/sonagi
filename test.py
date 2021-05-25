check = 0
while check == 0:
    try:
        f = open('recognition.txt', 'r')
        line = int(f.readline())
        # print(line)
        f.close()

        if line%1000 < 100:
            line = line + 100

        f = open('recognition.txt', 'w')
        f.write(str(line))
        f.close()

        check = 1
    except:
        continue