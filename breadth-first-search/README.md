# Breadth-first search

Breadth-First Search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at a chosen node (often called the 'root' in tree structures) and explores all its neighboring nodes at the present depth level before moving on to nodes at the next depth level. 

## Steps of the Algorithm:
1. **Start with the root node:** Mark it as visited and add it to the queue.
2. **Traverse neighbors:** For the node at the top of the queue, take it and go through all its unvisited neighbors.
3. **Recursive process:** For each unvisited neighbor, repeat the process: mark it as visited and add it to the queue.
4. **Completion:** The algorithm ends when the queue is empty.

Use FIFO (First In, First Out) data structure like a queue to keep track of the nodes to visit. The algorithm is implemented using recursion or an explicit queue data structure.
