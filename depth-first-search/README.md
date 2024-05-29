# Depth-first search

Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node and explores as far as possible along each branch before backtracking.

## Steps of the Algorithm:
1. **Start with the root node:** Mark it as visited and add it to the stack.
2. **Traverse neighbors:** For the node at the top of the stack, pop it and go through all its unvisited neighbors.
3. **Recursive process:** For each unvisited neighbor, repeat the process: mark it as visited and add it to the stack.
4. **Completion:** The algorithm ends when the stack is empty.

Use LIFO (Last In, First Out) data structure like a stack to keep track of the nodes to visit. The algorithm is implemented using recursion or an explicit stack data structure.
