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
    bitmask = (1<<size)-1
    for _ in xrange(size):
        result.append(i & bitmask)
        i >>= size
    print "\n".join(map(lambda x: format(x, "0{}b".format(size)), result)[::-1]), "\n"

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
    result.reverse()
    count = 0
    for i in reversed(xrange(M)):
        if not all(get_bit(bits, i) == 0 for bits in result):
            break
        count += 1
    while not result[0]:
        result.rotate(-1)
    return int("".join(map(lambda x: format(x<<count, "0{}b".format(M)), result)), 2)

def get_patterns(pattern):
    result = set()
    for is_reflect in [False, True]:
        if is_reflect:
            pattern = reflect(pattern)
        for _ in xrange(ROTATE_CYCLE):
            result.add(shift(pattern))
            #print_pattern(pattern)
            #print_pattern(shift(pattern))
            pattern = rotate(pattern)
    return tuple(sorted(result))

def add_pattern(state, pos, pattern):
    # TODO, check in grids, empty
    for i in xrange(M):
        if get_bit(pattern, i):
            break
    r, c = divmod(pos, N)
    if c < i:  # out of grids
        return 0
    c -= i
    for i in xrange(r, r+3):
        for j in xrange(c, c+3):
            if not get_bit(pattern, i*M+j):
                continue
            if j >= N or get_bit(state, i*N+j):
                return 0
            state = set_bit(state, i*N+j)
    return state

def get_placement(state, choices):
    # TODO, fill in by choices
    result = [['.' for _ in xrange(N)] for _ in xrange(N)]
    return result

def backtracking(patterns1, patterns2, curr, curr_state1, curr_state2, result1, result2):
    return True
    if curr == N and curr_state1 == curr_state2 == 0:
        return False  # no state in the first row, like shift up, impossible in the following search
    if curr_state1 == curr_state2 != 0:
        return True  # find a solution, right away return
    if curr == N*N:
        return False  # search to the end
    has_pattern1, has_pattern2 = get_bit(curr_state1, N*N-1-curr), get_bit(curr_state2, N*N-1-curr)
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
    for c1 in choices1:
        next_state1 = curr_state1
        if c1:
            next_state1 = add_pattern(curr_state1, curr, c1)
            if not next_state1:
                continue
            result1.append(c1)
        for c2 in choices2:
            next_state2 = curr_state1
            if c2:
                next_state2 = add_pattern(curr_state2, curr, c2)
                if not next_state2:
                    continue
                result2.append(c2)
            if backtracking(patterns1, patterns2, curr+1, next_state1, next_state2, result1, result2):
                return True
            if c2:
                result2.pop()
        if c1:
            result1.pop()
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
        start, state1, state2, result1, result2 = 0, 0, 0, [], []
        if backtracking(patterns1, patterns2, start, state1, state2, result1, result2):
            lookup[patterns1[0], patterns2[0]] = [get_placement(state1, result1), get_placement(state2, result2)]
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
