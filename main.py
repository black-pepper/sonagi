while True:
    try:
        f = open('recognition.txt', 'r')
        line = int(f.readline())
        f.close()

        if line%1000 >= 100:
            print(line)
            line -= 100

            f = open('recognition.txt', 'w')
            f.write(str(line))
            f.close()

    except:
        continue
