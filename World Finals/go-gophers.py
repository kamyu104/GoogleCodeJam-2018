# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2018 World Finals - Problem C. Go, Gophers!
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000007766/000000000004da2d
#
# Time:  O(M * (S + (S/W)^2)), W is tuned by testing, and larger W is not necessarily good
#                            , if W = 316, then S = (S/W)^2), O(M * (S + (S/W)^2)) = O(M * S)
#                            , but it uses 50% of S on average and worse than that of W = 25
# Space: O(S)
#

from sys import stdout
from collections import defaultdict
from itertools import islice
from random import randint, seed

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def print_line(s):
    print s
    stdout.flush()

def read_line():
    s = raw_input()
    if s == "-1":
        exit()
    return s

def query(queries, results, level, S):
    assert(len(queries)+W <= S)
    query = [level]*W
    queries += query
    print_line("\n".join(map(str, query)))
    for _ in xrange(W):
        results.append(int(read_line()))

def merge_sorted_lists(a, b):
    result = []
    i, j = 0, 0
    while i != len(a) or j != len(b):
        if j == len(b) or (i != len(a) and a[i][0] < b[j][0]):
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    return result

def check_candidate(queries, results, statistic, sorted_statistic, m):
    i = max((len(queries)-W)//m*m, 0)
    new_statistic = set()
    while i+m-1 < len(queries):
        i += m
        level = queries[i-m]
        if any(x != level for x in islice(queries, i-m, i)):
            continue
        count = sum((islice(results, i-m, i)))
        if level not in statistic:
            statistic[level] = count
            new_statistic.add((level, count))
            continue
        if statistic[level] != count:
            return
    assert(len(new_statistic) <= 1)
    if new_statistic:
        sorted_statistic[:] = merge_sorted_lists(sorted(new_statistic), sorted_statistic)
    curr_diff_intervals = []
    prev_level, prev_count, known_count, known_gcd = MIN_L-1, 0, 0, 0
    for curr_level, curr_count in sorted_statistic:
        if prev_count > curr_count:  # levels are not compressed by same count because they can be still checked in this case
            return
        if curr_count != prev_count:
            if prev_level+1 == curr_level:
                known_count += curr_count-prev_count
                known_gcd = gcd(known_gcd, curr_count-prev_count)
            curr_diff_intervals.append((prev_level, curr_level))  # even same level could be asked again
            prev_count = curr_count
        prev_level = curr_level  # increase prev_level even if count is same to make interval with shorter length
    if known_count == m and known_gcd != 1:
        return
    if m != prev_count:
        curr_diff_intervals.append((prev_level, MAX_L))
    return curr_diff_intervals

def check(candidates, queries, results, statistics, sorted_statistics):
    diff_intervals = set()
    for m in xrange(2, M+1):
        if m not in candidates:
            continue
        m_diff_intervals = check_candidate(queries, results, statistics[m], sorted_statistics[m], m)
        if not m_diff_intervals:
            candidates.pop(m)
            continue
        for m_diff_interval in m_diff_intervals:
            diff_intervals.add(m_diff_interval)
    if not diff_intervals:
        diff_intervals.add((MIN_L, MAX_L))
    return diff_intervals

def go_gophers():
    S = int(input())
    candidates = set(range(2, M+1))
    queries, results, statistics, sorted_statistics = [], [], defaultdict(dict), defaultdict(list)
    while True:
        diff_intervals = check(candidates, queries, results, statistics, sorted_statistics)
        if len(candidates) == 1:
            break
        level_set = set()
        for left, right in diff_intervals:
            for i in xrange(2):  # make left, right endpoints both have chance to be queried
                level_set.add((left+right+i)//2)
        level_set.discard(MIN_L-1)
        levels = list(level_set)
        query(queries, results, levels[randint(0, len(levels)-1)], S)  # add random to avoid worst case
    assert(len(queries) <= 0.1*S)  # 10% of S is used on average
    print_line(str(-next(iter(candidates))))

seed(0)
MIN_L, MAX_L = 1, 10**6
M = 25
W = M
T = int(input())
for case in xrange(T):
    go_gophers()
