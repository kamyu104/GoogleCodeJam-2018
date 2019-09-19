# [GoogleCodeJam 2018](https://codingcompetitions.withgoogle.com/codejam/archive/2018) ![Language](https://img.shields.io/badge/language-Python-orange.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE) ![Progress](https://img.shields.io/badge/progress-26%20%2F%2026-ff69b4.svg)

Python solutions of Google Code Jam 2018. Solution begins with `*` means it will get TLE in the largest data set (total computation amount > `10^8`, which is not friendly for Python to solve in 5 ~ 15 seconds).

* [Qualification Round](https://github.com/kamyu104/GoogleCodeJam-2018#qualification-round)
* [Round 1A](https://github.com/kamyu104/GoogleCodeJam-2018#round-1a)
* [Round 1B](https://github.com/kamyu104/GoogleCodeJam-2018#round-1b)
* [Round 1C](https://github.com/kamyu104/GoogleCodeJam-2018#round-1c)
* [Round 2](https://github.com/kamyu104/GoogleCodeJam-2018#round-2)
* [Round 3](https://github.com/kamyu104/GoogleCodeJam-2018#round-3)
* [World Finals](https://github.com/kamyu104/GoogleCodeJam-2018#world-finals)

## Qualification Round
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Saving The Universe Again](https://codingcompetitions.withgoogle.com/codejam/round/00000000000000cb/0000000000007966)| [Python](./Qualification%20Round/saving-the-universe-again.py)| _O(P)_ | _O(P)_ | Easy | | Greedy |
|B| [Trouble Sort](https://codingcompetitions.withgoogle.com/codejam/round/00000000000000cb/00000000000079cb)| [Python](./Qualification%20Round/trouble-sort.py)| _O(NlogN)_ | _O(N)_ | Easy | | Sort |
|C| [Go, Gopher!](https://codingcompetitions.withgoogle.com/codejam/round/00000000000000cb/0000000000007a30)| [Python](./Qualification%20Round/go-gopher.py)| _O(P)_ | _O(1)_ | Medium | | Probability, Simulation |
|D| [Cubic UFO](https://codingcompetitions.withgoogle.com/codejam/round/00000000000000cb/00000000000079cc)| [Python](./Qualification%20Round/cubic-ufo.py) |  _O(1)_ | _O(1)_ | Medium | | Rotation Matrix, Geometry |

## Round 1A
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Waffle Choppers](https://codingcompetitions.withgoogle.com/codejam/round/0000000000007883/000000000003005a)| [Python](./Round%201A/waffle-choppers.py)| _O(R * C)_ | _O(R + C)_ | Easy | | Array, Accumulation Sum |
|B| [Bit Party](https://codingcompetitions.withgoogle.com/codejam/round/0000000000007883/000000000002fff6)| [Python](./Round%201A/bit-party.py)| _O(ClogC * log(max(S)*B+max(P)))_ | _O(C)_ | Medium | | Binary Search |
|C| [Edgy Baking](https://codingcompetitions.withgoogle.com/codejam/round/0000000000007883/000000000002fff7)| [Python](./Round%201A/edgy-baking.py)| _O(N^2)_ | _O(N)_ | Medium | | Intervals |

## Round 1B
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Rounding Error](https://codingcompetitions.withgoogle.com/codejam/round/0000000000007764/0000000000036601)| [Python](./Round%201B/rounding-error.py)| _O(NlogN)_ | _O(N)_ | Medium | | Greedy, Memoization |
|B| [Mysterious Road Signs](https://codingcompetitions.withgoogle.com/codejam/round/0000000000007764/000000000003675b)| [Python](./Round%201B/mysterious-road-signs.py)| _O(S)_ | _O(1)_ | Medium | | Graph, Sliding Window |
|C| [Transmutation](https://codingcompetitions.withgoogle.com/codejam/round/0000000000007764/000000000003675c)| [C++](./Round%201B/transmutation.cpp) [PyPy](./Round%201B/transmutation.py)| _O(M^3 * logS)_ | _O(M^2)_ | Hard | | Binary Search, Overflow Pruning |

## Round 1C
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [A Whole New Word](https://codingcompetitions.withgoogle.com/codejam/round/0000000000007765/000000000003e064)| [Python](./Round%201C/a-whole-new-word.py)| _O(T)_ | _O(T)_ | Easy | | Trie |
|B| [Lollipop Shop](https://codingcompetitions.withgoogle.com/codejam/round/0000000000007765/000000000003e068)| [Python](./Round%201C/lollipop-shop.py)| _O(N^2)_ | _O(N)_ | Easy | | Probability |
|C| [Ant Stack](https://codingcompetitions.withgoogle.com/codejam/round/0000000000007765/000000000003e0a8)| [C++](./Round%201C/ant-stack.cpp) [PyPy](./Round%201C/ant-stack.py)| _O(N * K)_ | _O(K)_ | Medium | | DP |

## Round 2
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Falling Balls](https://codingcompetitions.withgoogle.com/codejam/round/0000000000007706/00000000000459f2)| [Python](./Round%202/falling-balls.py)| _O(C^2)_ | _O(C^2)_ | Easy | | Greedy |
|B| [Graceful Chainsaw Jugglers](https://codingcompetitions.withgoogle.com/codejam/round/0000000000007706/00000000000459f3)| [C++](./Round%202/graceful-chainsaw-jugglers.cpp) [PyPy](./Round%202/graceful-chainsaw-jugglers.py)| _O(R^(4/3)*B^(4/3))_ | _O(R * B)_ | Medium | | DP, Memoization |
|C| [Costume Change](https://codingcompetitions.withgoogle.com/codejam/round/0000000000007706/0000000000045875)| [C++](./Round%202/costume-change.cpp) [PyPy](./Round%202/costume-change.py)| _O(N^2 * sqrt(N))_ | _O(N)_ | Medium | | Bipartite Matching |
|D| [Gridception](https://codingcompetitions.withgoogle.com/codejam/round/0000000000007706/00000000000459f4)| [C++](./Round%202/gridception.cpp) [*PyPy](./Round%202/gridception.py)| _O(2^4 * R^2 * C^2)_ | _O(R * C)_ | Medium | | Graph, DFS |

## Round 3
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Field Trip](https://codingcompetitions.withgoogle.com/codejam/round/0000000000007707/000000000004b7fe)| [Python](./Round%203/field-trip.py)| _O(N)_ | _O(1)_ | Easy | | Greedy |
|B| [Name-Preserving Network](https://codingcompetitions.withgoogle.com/codejam/round/0000000000007707/000000000004ba29)| [Python](./Round%203/name-preserving-network.py)| _O(LlogL)_ | _O(L)_ | Medium | | Probability, Topology |
|C| [Raise the Roof](https://codingcompetitions.withgoogle.com/codejam/round/0000000000007707/000000000004b90d)| [Python](./Round%203/raise-the-roof.py)| _O(N^2)_ | _O(N)_ | Hard | | Geometry, Vector |
|D| [Fence Construction](https://codingcompetitions.withgoogle.com/codejam/round/0000000000007707/000000000004b90e)| [Python](./Round%203/fence-construction.py)| _O(FlogF)_ | _O(F)_ | Hard | | Dual Graph, Greedy |

## World Finals
You can relive the magic of the 2018 Code Jam World Finals by watching the [Live Stream Recording](https://www.youtube.com/watch?v=urT6rDu60h4) of the competition, problem explanations, interviews with Google and Code Jam engineers, and announcement of winners.

| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Jurisdiction Restrictions](https://codingcompetitions.withgoogle.com/codejam/round/0000000000007766/000000000004dbbd)| [PyPy](./World%20Finals/jurisdiction-restrictions.py) [PyPy](./World%20Finals/jurisdiction-restrictions2.py) | _O(S^6 * log(R * C))_ | _O(S^2)_ | Medium | | Dinic's Algorithm, Max-Flow Min-Cut Theorem, Binary Search, Inclusion-Exclusion Principle, Math |
|B| [Two-Tiling](https://codingcompetitions.withgoogle.com/codejam/round/0000000000007766/000000000004da97)| [Python](./World%20Finals/two-tiling.py) | _O((1+8+8+65)^(N^2))_ | _O(2^(2 * M^2 - 1) * N^2)_ | Hard | | Backtracking, Bit Manipulation, Union Find, Precompute |
|C| [Go, Gophers!](https://codingcompetitions.withgoogle.com/codejam/round/0000000000007766/000000000004da2d)| [Python](./World%20Finals/go-gophers.py) | _O(M * (S + (S/W)^2))_ | _O(S)_ | Medium | | Multiple Binary Searches |
|D| [Swordmaster](https://codingcompetitions.withgoogle.com/codejam/round/0000000000007766/000000000004d961)| [Python](./World%20Finals/swordmaster.py) | _O(N * P)_ | _O(N * P)_ | Hard | | BFS, DFS, DAG, SCC, Tarjan's Algorithm |
|E| [The Cartesian Job](https://codingcompetitions.withgoogle.com/codejam/round/0000000000007766/000000000004d962)| [Python](./World%20Finals/the-cartesian-job.py) | _O(K * N)_ | _O(N)_ | Hard | | DP, Intervals, Sort, Vector | 
