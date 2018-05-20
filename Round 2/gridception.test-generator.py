R, C = 3, 4
total = 0
for r in xrange(1, R+1):
    for c in xrange(1, C+1):
        total += 2**(r*c)
print total
for r in xrange(1, R+1):
    for c in xrange(1, C+1):
        def generate(i):
            colors = []
            for j in xrange(c):
                if i & (1 << j):
                    colors.append('B')
                else:
                    colors.append('W')
            print  "".join(colors)

        for i in xrange(2**(r*c)):
            print r, c
            for j in xrange(1, r+1):
                generate((i >> (r*c-j*c)) & (2**c-1))
