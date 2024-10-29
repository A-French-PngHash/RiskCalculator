

def calcul(n):
    count = 0
    for i in range(1, 7):
        count += 1 - (i / 6)**n
    count /= 6
    return count

cal = [calcul(3), calcul(2), calcul(1)]

print(cal[0] + (1-cal[0]) * (cal[1] + (1-cal[1]) * cal[2]))