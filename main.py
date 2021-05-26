check = 0
while True:
    try:
        f = open('recognition.txt', 'r')
        line = int(f.readline())
        f.close()
        total_sum = 0
        
        if line%100000 >= 11000:
            total_sum += 11000

        if line%1000 >= 100:
            total_sum += 100
            
        if line%100 >= 10:
            total_sum += 10

        if total_sum > 0:
            print(line)
            line -= total_sum
            f = open('recognition.txt', 'w')
            f.write(str(line))
            f.close()
            check = 0

    except:
        continue
