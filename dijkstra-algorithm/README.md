# Dijkstra's Algorithm

Dijkstra's algorithm is a graph search algorithm that finds the shortest path between a starting node and all other nodes in a weighted graph with non-negative edge weights. It is widely used in network routing protocols and geographic mapping applications.

## Steps of the Algorithm:
1. **Initialization:** Set the distance to the start node to 0 and to all other nodes to infinity. Add the start node to a priority queue with a distance of 0.
2. **Select the closest unvisited node:** Extract the node with the smallest distance from the priority queue. This node is the current node.
3. **Update neighboring nodes:** For each neighbor of the current node, calculate the distance from the start node to this neighbor through the current node. If this new distance is shorter than the previously known distance, update the shortest distance to this neighbor and add it to the priority queue.
4. **Mark the node as visited:** Once all neighbors of the current node have been processed, mark the current node as visited.
5. **Repeat:** Continue the process until the priority queue is empty.

The algorithm uses a priority queue to efficiently select the next node with the smallest tentative distance. It ensures that each node is visited in order of increasing distance from the start node.