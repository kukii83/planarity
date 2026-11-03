# ITS Graph Theory class Group 5 Assignment 9

Group 5 Members:

- Maulana Anugra Putra/5025251159 (kukii83)

- I Gusti Agung Candra Nugraha/5025251169 (candranugraha576)

- Hussein Mohammad Mahsun/5025251170 (TheDelightOFice)

---

In this project, we will use two algortihms, which is:

-Hopcroft Tarjan

---

## Hopcroft Tarjan
### Explanation
The Hopcroft–Tarjan algorithm is a linear-time $O(V)$ graph planarity testing algorithm that determines whether a graph can be drawn on a plane without its edges crossing. It operates by performing a Depth-First Search (DFS) to build a DFS tree, decomposing the graph into biconnected components, and tracking back-edges to evaluate whether the components can be successfully embedded without crossing paths. By systematically checking these structural constraints alongside Euler's formula bounds, it achieves optimal efficiency compared to brute-force subgraph or matrix-based approaches.

### Prerequisites
- Compiler(VSCode or any other that runs Python)
- Python 3.14

### Instructions
- Copy the code
- Open your compiler
- Open a new file and paste the code
- Run the code
- copy the sample input, and paste in the terminal
- Click enter, and click Ctrl + Z(for Windows) or Ctrl + D(for Mac), then click enter again, the program will show whether the graph is planar or non planar

### Results
Sample Input 1:
```bash
4 6
0 1
1 2
2 3
3 0
0 2
1 3
```
Sample Output 1:
```bash
--- Test Results ---
Graph Test Status : Graph is planar.
Is Planar?        : True
Total Edges Read  : 6
```

Sample Input 2:
```bash
6 9
1 0
0 3
5 4
4 3
3 2
2 1
0 5
5 2
4 1
```
Sample Output 2:
```bash
--- Test Results ---
Graph Test Status : Graph contains K3,3 or K5 non-planar subdivisions.
Is Planar?        : False
Total Edges Read  : 9
```

Sample Input 3:
```bash
6 9
1 0
0 three
5 4
4 3
3 2
2 1
0 5
5 2
4 1
```
Sample Output 3:
```bash
[Error] Invalid input format: invalid literal for int() with base 10: 'three'
```

---

Do your part guys

---
AI usage:
https://share.gemini.google/hiFZ93u9SorJ
