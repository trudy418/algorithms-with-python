class Node:
    def __init__(self, value):
        self.value = value
        self.subnodes = []

    def add(self, *args):
        for subnode in args:
            self.subnodes.append(subnode)


def depth_first_search(start_node, goal_node):
    visited = set()
    stack = [start_node]

    while stack:
        current_node = stack.pop()

        if current_node == goal_node:
            print(f"Goal: {current_node.value}")
            return True

        visited.add(current_node)
        print(f"Step: {current_node.value}")

        for subnode in current_node.subnodes:
            if subnode not in visited:
                stack.append(subnode)

    return False



if __name__ == '__main__':
    """
    0
    |\
    1 2
    |  \
    3   4
        |\
        5 6
           \
            7
    """
    nodes = []
    for i in range(8):
        nodes.append(Node(i))

    nodes[0].add(nodes[1], nodes[2])
    nodes[1].add(nodes[3])
    nodes[2].add(nodes[4])
    nodes[4].add(nodes[5], nodes[6])
    nodes[6].add(nodes[7])

    result = depth_first_search(nodes[0], nodes[3]) # 0 -> 2 -> 4 -> 6 -> 7 -> 5 -> 1 -> 3
    print(f"{'No solution.' if not result else 'Solution found.'}")