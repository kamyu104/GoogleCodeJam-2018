total = 0
for R in xrange(1, 4):
    for C in xrange(1, 5):
        total += 2**(R*C)
print total
for R in xrange(1, 4):
    for C in xrange(1, 5):
        def p(i):
            colors = []
            for j in xrange(C):
                if i & (1 << j):
                    colors.append('B')
                else:
                    colors.append('W')
            print  "".join(colors)

        for i in xrange(2**(R*C)):
            print R, C
            for j in xrange(1, R+1):
                p((i >> (R*C-j*C)) & (2**C-1))
