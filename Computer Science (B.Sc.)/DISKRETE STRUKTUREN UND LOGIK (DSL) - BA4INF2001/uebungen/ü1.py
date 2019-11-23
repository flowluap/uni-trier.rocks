
def T(n):
    menge=()
    for i in range(1, n + 1):
       if n % i == 0:
           menge += (i,)
    print("Die teilbare Menge von [{0}] = {1}".format(n,menge))
T(100)
