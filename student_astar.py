# student_astar.py
# ============================================================
# TASK
#   Implement A* search that returns (path, cost).
#
# SIGNATURE (do not change):
#   astar(start, goal, neighbors_fn, heuristic_fn, trace) -> (List[Coord], float)
#
# PARAMETERS
#   start, goal:           grid coordinates
#   neighbors_fn(u):       returns valid 4-neighbors of u
#   heuristic_fn(u, goal): returns a non-negative estimate to goal
#   trace:                 MUST call trace.expand(u) whenever you pop u
#                         from the PRIORITY QUEUE to expand it.
#
# EDGE COSTS
#   Assume unit step cost (=1) unless your runner specifies otherwise.
#   (If your runner supplies a graph.cost(u,v), adapt here if needed.)
#
# RETURN
#   (path, cost) where path is the list of coordinates from start to goal,
#   and cost is the sum of step costs along that path (float).
#   If no path exists, return ([], 0.0).
#
# IMPLEMENTATION HINT
# - Use min-heap over f = g + h.
# - Keep g[u] (cost from start), parent map, and a closed set.
# - On goal, reconstruct path and also compute cost (sum of steps).
# ============================================================

from typing import List, Tuple, Callable, Dict
import heapq

Coord = Tuple[int, int]

def astar(start: Coord,
          goal: Coord,
          neighbors_fn: Callable[[Coord], List[Coord]],
          heuristic_fn: Callable[[Coord, Coord], float],
          trace):
    """
    REQUIRED: call trace.expand(u) when you pop u from the PQ to expand.
    """
    if start == goal:
        return [start]

    g: Dict[Coord, float] = {start: 0.0}
    parent: Dict[Coord, Coord | None] = {start: None}
    heap: List[Tuple[float, Coord]] = []
    f0 = float(heuristic_fn(start, goal))
    heapq.heappush(heap, (f0, start))
    closed = set()

    while heap:
        _, u = heapq.heappop(heap)
        if u in closed:
            continue
        trace.expand(u)
        if u == goal:
            # reconstruct path
            path: List[Coord] = []
            cur: Coord | None = u
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            path.reverse()
            # unit edge costs → cost = steps = len(path)-1
            return path
        closed.add(u)

        for v in neighbors_fn(u):
            tentative = g[u] + 1.0
            if v not in g or tentative < g[v]:
                g[v] = tentative
                parent[v] = u
                f_v = tentative + float(heuristic_fn(v, goal))
                heapq.heappush(heap, (f_v, v))

    return []

# --- (ONLY IF YOUR RUNNER PASSES A Graph INSTEAD OF neighbors_fn) ---
# def astar_graph(graph, start, goal, heuristic_fn, trace):
#     return astar(start, goal, graph.neighbors, heuristic_fn, trace)
