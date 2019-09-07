# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2018 World Finals - Problem B. Two-Tiling
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000007766/000000000004da97
#
# Time:  O((1+8+8+65)^(N^2)), pass in PyPy2 but Python2
# Space: O(N^2)
#

from itertools import izip

def print_bin(i, size):
    result = []
    bitmask = (1<<size)-1
    for _ in xrange(size):
        result.append(i & bitmask)
        i >>= size
    result.reverse()
    print "\n".join(map(lambda x: format(x, "0{}b".format(size)), result)), "\n"

def print_pattern(i):
    print_bin(i, PATTERN_SIZE)

def print_state(i):
    print_bin(i, N)

def reflect(pattern):
    result = []
    bitmask = (1<<PATTERN_SIZE)-1
    for _ in xrange(PATTERN_SIZE):
        result.append(pattern & bitmask)
        pattern >>= PATTERN_SIZE
    return int("".join(map(lambda x: format(x, "0{}b".format(PATTERN_SIZE)), result)), 2)

def rotate(pattern):  # ccw rotate
    tmp = []
    bitmask = (1<<PATTERN_SIZE)-1
    for _ in xrange(PATTERN_SIZE):
        tmp.append(pattern & bitmask)
        pattern >>= PATTERN_SIZE
    result = [0]*PATTERN_SIZE
    bitmask = 1
    for bits in tmp:
        for i in xrange(PATTERN_SIZE):
            if bits & 1:
                result[i] |= bitmask
            bits >>= 1
        bitmask <<= 1
    return int("".join(map(lambda x: format(x, "0{}b".format(PATTERN_SIZE)), result)), 2)

def shift(pattern):  # shift to left-up most
    return pattern

def get_patterns(pattern):
    result = set()
    for is_reflect in [False, True]:
        if is_reflect:
            pattern = reflect(pattern)
        for _ in xrange(ROTATE_CYCLE):
            pattern = rotate(pattern)
            result.add(shift(pattern))
    return tuple(sorted(result))

def add_pattern(state, pos, pattern):
    # TODO
    return state  # 0 if invalid

def get_placement(state, get_patterns, choices):
    # TODO
    result = ['*'*N for _ in xrange(N)]
    return result

def backtracking(patterns1, patterns2, curr, curr_state1, curr_state2, result1, result2):
    if curr == N and curr_state1 == curr_state2 == 0:
        return False  # shift up, impossible in the following search
    if curr_state1 == curr_state2 != 0:
        return True  # find a solution, right away return
    if curr == len(BITMASKS):
        return False  # search to the end
    has_pattern1, has_pattern2 = BITMASKS[curr]&curr_state1, BITMASKS[curr]&curr_state2
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
    for i, p1 in enumerate(choices1):
        next_state1 = curr_state1
        if p1:
            next_state1 = add_pattern(curr_state1, i, p1)
            if not next_state1:
                continue
            result1.append(i)
        for j, p2 in enumerate(choices2):
            next_state2 = curr_state1
            if p2:
                next_state2 = add_pattern(curr_state2, i, p2)
                if not next_state2:
                    continue
                result2.append(j)
            if backtracking(patterns1, patterns2, curr+1, next_state1, next_state2, result1, result2):
                return True
            if p2:
                result2.pop()
        if p1:
            result1.pop()
    return False

def two_tiling():
    pattern1, pattern2 = [0 for _ in xrange(PATTERN_SIZE)], [0 for _ in xrange(PATTERN_SIZE)]
    for i in xrange(PATTERN_SIZE):
        pattern1[i], pattern2[i] = raw_input().strip().split(' ')
    patterns1, patterns2 = map(get_patterns,
                               map(lambda x: int("".join(x).replace('.', '0').replace('@', '1'), 2), 
                                   [pattern1, pattern2]))
    is_swapped = False
    if patterns1[0] > patterns2[0]:
        is_swapped = True
        patterns1, patterns2 = patterns2, patterns1
    if (patterns1[0], patterns2[0]) not in lookup:
        lookup[patterns1[0], patterns2[0]] = []
        start, state1, state2, result1, result2 = 0, 0, 0, [], []
        if backtracking(patterns1, patterns2, start, state1, state2, result1, result2):
            lookup[patterns1[0], patterns2[0]] = [get_placement(state1, patterns1, result1), \
                                                  get_placement(state2, patterns2, result2)]
    result = lookup[patterns1[0], patterns2[0]]
    if is_swapped:
        result.reverse()
    return "IMPOSSIBLE" if not result else \
            "\n".join(["POSSIBLE", "\n".join(" ".join(pair) for pair in izip(*result))])

N = 8
PATTERN_SIZE = 3
ROTATE_CYCLE = 4
BITMASKS = [0]*(N**2)
bitmask = 1
for i in reversed(xrange(len(BITMASKS))):
    BITMASKS[i] = bitmask
    bitmask <<= 1
lookup = {}
for case in xrange(input()):
    if case: raw_input()  # skip empty line
    print 'Case #%d: %s' % (case+1, two_tiling())
