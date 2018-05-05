# time python ant-stack.test-generator.py | python ant-stack.py

import random

T = 100
W = 10**9

print T
for _ in xrange(6):
    N = 10**5
    print N
    Ws = []
    for i in xrange(N):
        Ws.append(str(random.randint(0,W)))
    print " ".join(Ws)
for _ in xrange(T-6):
    N = random.randint(2, 500)
    print N
    Ws = []
    for i in xrange(N):
        Ws.append(str(random.randint(1,W)))
    print " ".join(Ws)
