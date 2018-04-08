# Time:  O(SlogS), S is the count of 'S'
# Space: O(S)

import heapq

def parse(P):
    max_heap, count = [], 0
    for c in P:
        if c == 'C':
            count += 1
        else:
            heapq.heappush(max_heap, -count)
    return max_heap

def saving_the_universe_again():
    D, P = raw_input().strip().split()
    D = int(D)
    max_heap = parse(P)

    hacks, to_reduce = 0, sum(map(lambda(x): 2**-x, max_heap))-D
    while max_heap:
        if to_reduce <= 0:
            break
        count = heapq.heappop(max_heap)
        if count == 0:
            break
        count += 1
        to_reduce -= 2**-count
        hacks += 1
        if count:
            heapq.heappush(max_heap, count)

    return hacks if to_reduce <= 0 else "IMPOSSIBLE"

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, saving_the_universe_again())
