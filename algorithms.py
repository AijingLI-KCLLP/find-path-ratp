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

        for neighbor_id, travel_time in get_neighbors(current_node_id):
            if neighbor_id in closed_list:
                continue

            tentative_g = current_node['g']+travel_time

            # create neighbor
            if neighbor_id not in open_dict:
                neighbor_node = create_node_A_star(neighbor_id, g=tentative_g, h=heuristics(neighbor_id,end),parent=current_node)
                heapq.heappush(open_heap, (neighbor_node['f'],neighbor_node['id'],))
                open_dict[neighbor_id] = neighbor_node
            # updaate neighbor
            elif tentative_g < open_dict[neighbor_id]['g']:
                neighbor_node = open_dict[neighbor_id]
                neighbor_node['g'] = tentative_g
                neighbor_node['f'] = tentative_g + neighbor_node['h']
                neighbor_node['parent'] = current_node
                heapq.heappush(open_heap, (neighbor_node['f'], neighbor_node['id']))

    return [] # no path


def create_node_A_star(station_id, g=float('inf'), h=0.0, parent=None):
    return {
        'id': station_id,
        'g': g,
        'h': h,
        'f': g+h,
        'parent': parent
    }

def reconstruct_path(end_node):
    path = []
    current = end_node

    while current is not None:
        path.append(current)
        current = current['parent']

    return path[::-1]
