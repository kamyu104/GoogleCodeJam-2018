# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Round 1B - Problem A. Rounding Error
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000007764/0000000000036601
#
# Time:  O(NlogN)
# Space: O(N)
#

def min_votes_to_round(N, i, lookup):
    if i >= N:
        return 0
    if lookup[i] != -1:
        return lookup[i]
    if i == 0 or 0 < 100*i % N < (N+1)/2:
        lookup[i] = min_votes_to_round(N, i+1, lookup)+1
    else:
        lookup[i] = 0
    return lookup[i]

def rounding_error():
    N, L = map(int, raw_input().strip().split())
    C = map(int, raw_input().strip().split())

    lookup = [-1] * N
    remaining_votes = N-sum(C)
    additional_votes = []
    for i in xrange(len(C)):
        if 0 < min_votes_to_round(N, C[i], lookup) <= remaining_votes:
            additional_votes.append((min_votes_to_round(N, C[i], lookup), i))
    additional_votes.sort()

    for votes, i in additional_votes:
        if votes > remaining_votes:
            break
        remaining_votes -= votes
        C[i] += votes

    C.extend([min_votes_to_round(N, 0, lookup)]*(remaining_votes/(min_votes_to_round(N, 0, lookup))))
    remaining_votes %= min_votes_to_round(N, 0, lookup)
    if remaining_votes:
        C.append(remaining_votes)

    result = 0
    for i in C:
        result += (100*i + N/2) / N
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, rounding_error())
