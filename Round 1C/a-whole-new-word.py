# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Round 1C - Problem A. A Whole New Word
# https://codejam.withgoogle.com/2018/challenges/0000000000007765/dashboard
#
# Time:  O(T), T is the number of nodes in trie
# Space: O(T)
#

import collections
import functools

def dfs(trie, lookup, i, curr):
    if i == len(lookup):
        return "-"
    if len(trie) != len(lookup[i]):
        for c in lookup[i]:
            if c not in trie:
                curr.append(c)
                nodes = trie.values()[0]
                while nodes:
                    c = nodes.keys()[0]
                    curr.append(c)
                    nodes = nodes[c]
                break
        return "".join(curr)
    for c in trie:
        curr.append(c)
        result = dfs(trie[c], lookup, i+1, curr)
        curr.pop()
        if result != "-":
            return result
    return "-"

def a_whole_new_word():
    _trie = lambda: collections.defaultdict(_trie)
    trie = _trie()
    N, L = map(int, raw_input().strip().split())
    lookup = [set() for _ in xrange(L)]
    for _ in xrange(N):
        word = raw_input().strip()
        for i in xrange(L):
            lookup[i].add(word[i])
        functools.reduce(dict.__getitem__, word, trie)
    return dfs(trie, lookup, 0, [])

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, a_whole_new_word())
