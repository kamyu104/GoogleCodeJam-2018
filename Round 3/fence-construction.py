# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Round 3 - Problem D. Fence Construction
# https://codejam.withgoogle.com/2018/challenges/0000000000007707/dashboard/000000000004b90e
#
# Time:  O(FlogF)
# Space: O(F)
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
def dual_graph(edges):
    # pre-process
    adj_nodes = collections.defaultdict(list)
    for edge in edges:
        adj_nodes[edge[0]].append(edge[1])
        adj_nodes[edge[1]].append(edge[0])
    for node in adj_nodes:
        adj_nodes[node].sort(key=lambda x: clockwiseangle_and_distance(x, node))  # Time: O(FlogF)
    inv_idx_adj_nodes = collections.defaultdict(lambda: collections.defaultdict(int))
    for node in adj_nodes:
        for i in xrange(len(adj_nodes[node])):
            inv_idx_adj_nodes[node][adj_nodes[node][i]] = i

    # process
    edgeset = set()
    for edge in edges:
        edge = list(edge)
        edgeset |= set([(edge[0],edge[1]),(edge[1],edge[0])])
    face_paths = []
    path  = []
    for edge in edgeset:
        path.append(edge)
        edgeset -= set([edge])
        break
    while edgeset:
        neighbors = adj_nodes[path[-1][-1]]
        inv_idx_neighbors = inv_idx_adj_nodes[path[-1][-1]]
        next_node = neighbors[(inv_idx_neighbors[path[-1][-2]]+1)%(len(neighbors))]
        tup = (path[-1][-1],next_node)
        if tup == path[0]:
            face_paths.append(path)
            path = []
            for edge in edgeset:
                path.append(edge)
                edgeset -= set([edge])
                break
        else:
            path.append(tup)
            edgeset -= set([tup])
    if path:
        face_paths.append(path)

    # post-process
    inv_idx_edges = collections.defaultdict(lambda: collections.defaultdict(int))
    for i, e in enumerate(edges):
        inv_idx_edges[(e[0], e[1])] = i
        inv_idx_edges[(e[1], e[0])] = i    
    edge_faces = collections.defaultdict(list)
    face_edges = []
    for i, path in enumerate(face_paths):
        face_edge = set()
        for node in path:
            face_edge.add(inv_idx_edges[node])
        face_edges.append(face_edge)
        for edge in face_edge:
            edge_faces[edge].append(i)
    return edge_faces, face_edges

def fence_construction():
    F, K = map(int, raw_input().strip().split())
    edges = [None]*F
    for i in xrange(F):
        A, B, C, D = map(int, raw_input().strip().split())
        edges[i] = [(A, B), (C, D)]
            
    edge_faces, face_edges = dual_graph(edges)  

    result = []
    visited_faces = set()
    visited_edges = set([K-1])
    max_heap = [-(K-1)]
    while max_heap:
        i = -heapq.heappop(max_heap)  # Time: O(FlogF)
        result.append(i+1)
        for face in edge_faces[i]:
            if face in visited_faces:
                continue
            visited_faces.add(face)
            for nei in face_edges[face]:
                if nei in visited_edges:
                    continue
                visited_edges.add(nei)
                heapq.heappush(max_heap, -nei)
    result.reverse()              
    return " ".join(map(str, result))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, fence_construction())
