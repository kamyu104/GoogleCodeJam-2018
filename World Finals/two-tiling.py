# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2018 World Finals - Problem B. Two-Tiling
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000007766/000000000004da97
#
# Time:  O((1+8+8+65)^(N^2)), pass in PyPy2 but Python2
# Space: O(N^2)
#

from collections import deque
from itertools import izip

def print_bin(i, size):
    result = []
    bitmask = BITMASKS[size]-1
    for _ in xrange(size):
        result.append(i & bitmask)
        i >>= size
    print "\n".join(map(lambda x: format(x, "0{}b".format(size))[::-1], result)), "\n"

def print_pattern(i):
    print_bin(i, M)

def print_state(i):
    print_bin(i, N)

def get_bit(bits, i):
    return int(bits&BITMASKS[i] != 0)

def set_bit(bits, i):
    return bits|BITMASKS[i]

def reflect(pattern):
    result = []
    bitmask = (1<<M)-1
    for _ in xrange(M):
        result.append(pattern & bitmask)
        pattern >>= M
    return int("".join(map(lambda x: format(x, "0{}b".format(M)), result)), 2)

def rotate(pattern):  # ccw rotate
    tmp = []
    bitmask = (1<<M)-1
    for _ in xrange(M):
        tmp.append(pattern & bitmask)
        pattern >>= M
    result = [0]*M
    for j, bits in enumerate(tmp):
        for i in xrange(M):
            if get_bit(bits, i):
                result[i] = set_bit(result[i], j)
    return int("".join(map(lambda x: format(x, "0{}b".format(M)), result)), 2)

def shift(pattern):  # shift to left-up most
    assert(pattern != 0)
    result = deque()
    bitmask = BITMASKS[M]-1
    for _ in xrange(M):
        result.append(pattern & bitmask)
        pattern >>= M
    count = 0
    for i in xrange(M):
        if not all(get_bit(bits, i) == 0 for bits in result):
            break
        count += 1
    while not result[0]:
       result.rotate(-1)
    result.reverse()
    return int("".join(map(lambda x: format(x>>count, "0{}b".format(M)), result)), 2)

def get_patterns(pattern):
    result = set()
    for is_reflect in [False, True]:
        if is_reflect:
            pattern = reflect(pattern)
        for _ in xrange(ROTATE_CYCLE):
            result.add(shift(pattern))
            # print_pattern(pattern)
            # print_pattern(shift(pattern))
            # print "-"*5
            pattern = rotate(pattern)
    return tuple(sorted(result))

def add_pattern(state, pos, pattern):
    prev = state
    for i in xrange(M):
        if get_bit(pattern, i):
            break
    r, c = divmod(pos, N)
    if c < i:  # out of grids
        return 0
    c -= i
    for i in xrange(M):
        for j in xrange(M):
            if not get_bit(pattern, i*M+j):
                continue
            if r+i >= N or c+j >= N or get_bit(state, (r+i)*N+(c+j)):
                return 0
            state = set_bit(state, (r+i)*N+(c+j))
    # print pos
    # print_state(prev), print_pattern(pattern), print_state(state)
    return state

def get_placement(state, choices):
    # print_state(state)
    result = []
    bitmask = BITMASKS[N]-1
    for _ in xrange(N):
        result.append(state & bitmask)
        state >>= N
    result = map(lambda x: list(format(x, "0{}b".format(N))[::-1].replace('0', '.').replace('1', '@')), result)
    return result

def backtracking(patterns1, patterns2, curr, curr_state1, curr_state2, result1, result2):
    # return False
    # print curr
    # print_state(curr_state1), print_state(curr_state2)
    # print '-'*5
    if curr == N and curr_state1[0] == curr_state2[0] == 0:
        return False  # no state in the first row, like shift up, impossible in the following search
    if curr_state1[0] == curr_state2[0] != 0:
        #print curr, result1, result2
        return True  # find a solution, right away return
    if curr == N*N:
        return False  # search to the end
    has_pattern1, has_pattern2 = get_bit(curr_state1[0], curr), get_bit(curr_state2[0], curr)
    if has_pattern1 and has_pattern2:  # A, B
        return backtracking(patterns1, patterns2, curr+1, curr_state1, curr_state2, result1, result2)
    if not has_pattern1 and not has_pattern2:  # empty
        if backtracking(patterns1, patterns2, curr+1, curr_state1, curr_state2, result1, result2):
            return True
    choices1, choices2 = [0], [0]
    if not has_pattern1:
        choices1 = patterns1
    if not has_pattern2:
        choices2 = patterns2
    #print choices1, choices2
    for c1 in choices1:
        # print curr
        # print_state(curr_state1)
        # print_pattern(c1)
        if c1:
            next_state1 = add_pattern(curr_state1[0], curr, c1)
            if not next_state1:
                continue
            prev_state1 = curr_state1[0]
            curr_state1[0] = next_state1
            result1.append(c1)
        for c2 in choices2:
            # print_pattern(c2)
            if c2:
                next_state2 = add_pattern(curr_state2[0], curr, c2)
                if not next_state2:
                    continue
                prev_state2 = curr_state2[0]
                curr_state2[0] = next_state2
                result2.append(c2)
            if backtracking(patterns1, patterns2, curr+1, curr_state1, curr_state2, result1, result2):
                return True
            if c2:
                result2.pop()
                curr_state2[0] = prev_state2
        if c1:
            result1.pop()
            curr_state1[0] = prev_state1
    return False

def two_tiling():
    pattern1, pattern2 = [0 for _ in xrange(M)], [0 for _ in xrange(M)]
    for i in xrange(M):
        pattern1[i], pattern2[i] = raw_input().strip().split(' ')
    patterns1, patterns2 = map(get_patterns,
                               map(lambda x: int("".join(x).replace('.', '0').replace('@', '1')[::-1], 2), 
                                   [pattern1, pattern2]))
    #map(print_pattern, patterns1)
    is_swapped = False
    if patterns1[0] > patterns2[0]:
        is_swapped = True
        patterns1, patterns2 = patterns2, patterns1
    if (patterns1[0], patterns2[0]) not in lookup:
        lookup[patterns1[0], patterns2[0]] = []
        start, state1, state2, result1, result2 = 0, [0], [0], [], []
        if backtracking(patterns1, patterns2, start, state1, state2, result1, result2):
            lookup[patterns1[0], patterns2[0]] = [get_placement(state1[0], result1), get_placement(state2[0], result2)]
    result = lookup[patterns1[0], patterns2[0]]
    if is_swapped:
        result.reverse()
    return "IMPOSSIBLE" if not result else \
            "\n".join(["POSSIBLE", "\n".join(" ".join(map(lambda x: "".join(x), pair)) for pair in izip(*result))])

N = 8
CHAR_SET = "!?0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
M = 3
ROTATE_CYCLE = 4
BITMASKS = [0]*(N**2)
bitmask = 1
for i in xrange(len(BITMASKS)):
    BITMASKS[i] = bitmask
    bitmask <<= 1
lookup = {}
for case in xrange(input()):
    if case: raw_input()  # skip empty line
    print 'Case #%d: %s' % (case+1, two_tiling())
