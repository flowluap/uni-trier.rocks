def calcM1(m1):
    for element in m1:
        if element+3 not in m1:
            m1.append(element+3)
                
        if element+5 not in m1:
            m1.append(element+5)

        print(sorted(m1))

def calcM2(m2):
    for element in m2:
        if element+3 not in m2:
            m2.append(element+3)

        print(sorted(m2))

if __name__ == "__main__":
    calcM1([3,4])
    #calcM2([3,4,8])
