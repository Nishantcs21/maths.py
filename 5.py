def dijkstra(graph, start, end):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    previous = {}
    unvisited = set(graph)
    current = start
    while current != end:
        for neighbor in graph[current]:
            new_distance = distances[current] + graph[current][neighbor]
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current
        unvisited.remove(current)
        if not unvisited:
            return None, None
        candidates = {node: distances[node] for node in unvisited}
        current = min(candidates, key=candidates.get)
    path = []
    while current != start:
        path.append(current)
        current = previous[current]
    path.append(start)
    path.reverse()
    return path, distances[end]
graph = {"A": {"B": 7, "C": 3, "D":2, "E":2},"B": {"A": 7, "C": 1},"C": {"A": 3, "B": 1, "E": 4,"F":3},"D": {"A": 2,
"E": 1,"G":2,"F":10},"E": {"A":2,"C":4,"D":1,"F":4,"G":2},"F": {"C":3,"D":10,"E":4,"G":7},"G": {"D":2,"E":2,"F":7}}
shortest_path, shortest_distance = dijkstra(graph, "B", "G")
print("Shortest Path: ", shortest_path)
print("Shortest Distance: ", shortest_distance)