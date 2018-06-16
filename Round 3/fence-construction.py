# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Round 3 - Problem D. Fence Construction
# https://codejam.withgoogle.com/2018/challenges/0000000000007707/dashboard
#
# Time:  O(NlogN)
# Space: O(N)
#

import collections
import heapq
import math

def clockwiseangle_and_distance(point, origin):
    refvec = [0, 1]
    vector = [point[0]-origin[0], point[1]-origin[1]]
    lenvector = math.hypot(vector[0], vector[1])
    if lenvector == 0:
        return -math.pi, 0
    normalized = [vector[0]/lenvector, vector[1]/lenvector]
    dotprod  = normalized[0]*refvec[0] + normalized[1]*refvec[1]
    diffprod = refvec[1]*normalized[0] - refvec[0]*normalized[1]
    angle = math.atan2(diffprod, dotprod)
    if angle < 0:
        return 2*math.pi+angle, lenvector
    return angle, lenvector

# Time:  O(FlogF)
# Space: O(F)
def get_faces(edges):
    embedding = collections.defaultdict(list)
    for e in edges:
        embedding[e[0]].append(e[1])
        embedding[e[1]].append(e[0])
    for node in embedding:
        embedding[node].sort(key=lambda x: clockwiseangle_and_distance(x, node))
    inv_idx_embedding = collections.defaultdict(lambda: collections.defaultdict(int))
    for node in embedding:
        for i in xrange(len(embedding[node])):
            inv_idx_embedding[node][embedding[node][i]] = i

    edgeset = set()
    for edge in edges:
        edge = list(edge)
        edgeset |= set([(edge[0],edge[1]),(edge[1],edge[0])])
    faces = []
    path  = []
    for edge in edgeset:
        path.append(edge)
        edgeset -= set([edge])
        break
    while edgeset:
        neighbors = embedding[path[-1][-1]]
        inv_idx_neighbors = inv_idx_embedding[path[-1][-1]]
        next_node = neighbors[(inv_idx_neighbors[path[-1][-2]]+1)%(len(neighbors))]
        tup = (path[-1][-1],next_node)
        if tup == path[0]:
            faces.append(path)
            path = []
            for edge in edgeset:
                path.append(edge)
                edgeset -= set([edge])
                break
        else:
            path.append(tup)
            edgeset -= set([tup])
    if path:
        faces.append(path)
    return faces

def fence_construction():
    K, F = map(int, raw_input().strip().split())
    fences, edges = [None] * K, []
    inv_idx_fences = collections.defaultdict(lambda: collections.defaultdict(int))
    for i in xrange(K):
        A, B, C, D = map(int, raw_input().strip().split())
        edges.append([(A, B), (C, D)])
        fences[i] = [(A, B), (C, D)]
        inv_idx_fences[((A, B), (C, D))] = i
        inv_idx_fences[((C, D), (A, B))] = i
            
    faces = get_faces(edges)  
    fence_faces = collections.defaultdict(list)
    face_sets = []
    for i, face in enumerate(faces):
        fence_face = set()
        for n in face:
            fence_face.add(inv_idx_fences[n])
        face_sets.append(fence_face)
        for j in fence_face:
            fence_faces[j].append(i)

    result = []
    visited = set([F-1])
    max_heap = [-(F-1)]
    while max_heap:
        i = -heapq.heappop(max_heap)
        result.append(i+1)
        for face in fence_faces[i]:
            for nei in face_sets[face]:
                if nei not in visited:
                    visited.add(nei)
                    heapq.heappush(max_heap, -nei)
            face_sets[face] = set()
    result.reverse()              
    return " ".join(map(str, result))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, fence_construction())
