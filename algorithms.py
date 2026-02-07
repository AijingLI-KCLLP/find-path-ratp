from stations import get_station_by_id
import heapq
from reseau import heuristics, get_neighbors, get_adjacency_matrix

def A_star(start, end):
    start_node_A_star = create_node_A_star(start, g=0, h=heuristics(start,end))

    open_heap = [(start_node_A_star['f'],start_node_A_star['id'],)] # priority queue
    open_dict = {start_node_A_star['id']: start_node_A_star} #  fetch quickly node_A_star
    closed_list = set()

    while open_heap:
        _, current_node_id = heapq.heappop(open_heap)
        current_node = open_dict[current_node_id]

        if current_node_id == end :
            return reconstruct_path(current_node)

        closed_list.add(current_node_id)





    return None


def create_node_A_star(station_id, g=float('inf'), h=0.0, parent=None):
    return {
        'station_id': station_id,
        'g': g,
        'h': h,
        'f': g+h,
        'parent': parent
    }

def reconstruct_path(end_node):
    path = []
    current = end_node

    while end_node is not None:
        path.append(end_node)
        current = current['parent']

    return path[::-1]