# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Round 1A - Problem A. Waffle Choppers
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000007883/000000000003005a
#
# Time:  O(R * C)
# Space: O(R * C)
#

def calc_accus(waffle, R, C):
    accus = [[0]*C for _ in xrange(R)]
    for r in xrange(R):
        if r == 0:
            accus[r][0] = int(waffle[r][0] == '@')
        else:
            accus[r][0] = int(waffle[r][0] == '@') + \
                          accus[r-1][0]
        for c in xrange(1, C):
            if r == 0:
                accus[r][c] = int(waffle[r][c] == '@') + \
                              accus[r][c-1]
            else:
                accus[r][c] = int(waffle[r][c] == '@') + \
                              accus[r-1][c] + \
                              accus[r][c-1] - \
                              accus[r-1][c-1]
    return accus

def cut(accus, count_to_cut, cut_idxs):
    count = count_to_cut
    for i, accu in enumerate(accus):
        if accu == count:
            cut_idxs.append(i)
            count += count_to_cut
        elif accu > count:
            return False
    return True

def check_equal(accus, h_cut_idxs, v_cut_idxs):
    for r in xrange(len(h_cut_idxs)):
        if r == 0:
            count = accus[h_cut_idxs[r]][v_cut_idxs[0]]
        else:
            if count != \
               accus[h_cut_idxs[r]][v_cut_idxs[0]] - \
               accus[h_cut_idxs[r-1]][v_cut_idxs[0]]:
               return False
        for c in xrange(1, len(v_cut_idxs)):
            if r == 0:
                if count != \
                   accus[h_cut_idxs[r]][v_cut_idxs[c]] - \
                   accus[h_cut_idxs[r]][v_cut_idxs[c-1]]:
                    return False
            else:
                if count != \
                   accus[h_cut_idxs[r]][v_cut_idxs[c]] - \
                   accus[h_cut_idxs[r-1]][v_cut_idxs[c]] - \
                   accus[h_cut_idxs[r]][v_cut_idxs[c-1]] + \
                   accus[h_cut_idxs[r-1]][v_cut_idxs[c-1]]:
                    return False
    return True

def waffle_hoppers():
    R, C, H, V = map(int, raw_input().strip().split())
    waffle = []
    for r in xrange(R):
        waffle.append(list(raw_input().strip()))

    accus = calc_accus(waffle, R, C)
    if accus[-1][-1] != 0:
        h_count_to_cut, h_remain = divmod(accus[-1][-1], H+1)
        h_cut_idxs = []
        if h_remain != 0 or not cut([accus[r][-1] for r in xrange(R)], h_count_to_cut, h_cut_idxs):
            return "IMPOSSIBLE"

        v_count_to_cut, v_remain = divmod(accus[-1][-1], V+1)
        v_cut_idxs = []
        if v_remain != 0 or not cut(accus[-1], v_count_to_cut, v_cut_idxs):
            return "IMPOSSIBLE"

        if not check_equal(accus, h_cut_idxs, v_cut_idxs):
            return "IMPOSSIBLE"

    return "POSSIBLE"

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, waffle_hoppers())
