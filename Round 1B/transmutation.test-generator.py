import random

T = 100
G = 10**9

print T
for _ in xrange(T):
    M = random.randint(2, 100)
    print M
    for i in xrange(M):
        R1 = random.randint(1,M-1)
        R2 = random.randint(R1+1, M)
        print R1, R2
    Gs = []
    for i in xrange(M):
        Gs.append(str(random.randint(0,G)))
    print " ".join(Gs)
