# Create a program to find the shortest path from a given vertex to all other vertices
# in a graph using Dijkstra's algorithm.
# use adjacency list representation of the graph
from queue import PriorityQueue


def dijkstra(graph, source):
    # initialize distance to all vertices as infinity
    distance = {vertex: float('inf') for vertex in graph}
    # distance from source to source is 0
    distance[source] = 0
    # initialize empty set of visited vertices
    visited = set()
    # initialize empty priority queue
    queue = PriorityQueue()
    # add source to queue
    queue.put((0, source))
    # while queue is not empty
    while not queue.empty():
        # remove vertex with minimum distance from queue
        current_distance, current_vertex = queue.get()
        # if vertex has already been visited, ignore it
        if current_vertex in visited:
            continue
        # for each neighbor of the vertex
        for neighbor, weight in graph[current_vertex].items():
            # if neighbor has not been visited
            if neighbor not in visited:
                # calculate distance to neighbor through current vertex
                distance_through_current_vertex = current_distance + weight
                # if distance to neighbor through current vertex is less than distance to neighbor
                if distance_through_current_vertex < distance[neighbor]:
                    # update distance to neighbor
                    distance[neighbor] = distance_through_current_vertex
                    # add neighbor to queue
                    queue.put((distance_through_current_vertex, neighbor))
        # add vertex to visited set
        visited.add(current_vertex)
    # return distance to all vertices by multiplying by -1
    return {vertex: distance[vertex] * -1 for vertex in distance}


# main
if __name__ == '__main__':
    # create graph
    graph = {'A': {'B': 5},
             'B': {'E': 2, 'F': 5},
             'C': {},
             'D': {'C': 20},
             'E': {'C': 10},
             'F': {'C': 50, 'D': 2}}

    # negate all weights
    for vertex in graph:
        for neighbor in graph[vertex]:
            graph[vertex][neighbor] *= -1
    # get source vertex
    source = input('Enter source vertex: ')
    # get distance to all vertices
    distance = dijkstra(graph, source)
    # print distance to all vertices
    print('Distance from {} to all other vertices:'.format(source))
    for vertex, d in distance.items():
        print('{}: {}'.format(vertex, d))
