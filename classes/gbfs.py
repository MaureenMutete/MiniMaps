import heapq

class GBFSTraverser:
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic
        self.visited = []

    def GBFS(self, start, goal):
        priority_queue = [(self.heuristic[start], start)]
        while priority_queue:
            _, current_node = heapq.heappop(priority_queue)
            if current_node == goal:
                self.visited.append(current_node)
                return True
            if current_node not in self.visited:
                self.visited.append(current_node)
            neighbors = list(self.graph.neighbors(current_node))
            neighbors = [n for n in neighbors if n not in self.visited]
            for neighbor in neighbors:
                heapq.heappush(priority_queue, (self.heuristic[neighbor], neighbor))
        return False
