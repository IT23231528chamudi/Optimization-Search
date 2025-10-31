import json
from collections import deque

# Load problem
data = json.load(open('problem.json'))
obstacles = set(tuple(o) for o in data['obstacles'])

def neighbors_fn(u):
    r, c = u
    out = []
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 6 and 0 <= nc < 6 and (nr, nc) not in obstacles:
            out.append((nr, nc))
    return out

# Reference BFS (exact copy from runner)
def ref_bfs(start, goal):
    if start == goal: return [start]
    q = deque([start])
    parent = {start: None}
    while q:
        u = q.popleft()
        print(f"Pop u={u}")
        for v in neighbors_fn(u):
            if v not in parent:
                parent[v] = u
                print(f"  Discover v={v}, parent[{v}]={u}")
                if v == goal:
                    print(f"  Found goal at v={v}")
                    p = [v]
                    print(f"  Start path: {p}")
                    while parent[p[-1]] is not None:
                        print(f"    parent[{p[-1]}]={parent[p[-1]]}")
                        p.append(parent[p[-1]])
                        print(f"    Path now: {p}")
                    print(f"  After while loop: {p}")
                    p.append(start)
                    print(f"  After append start: {p}")
                    p.reverse()
                    print(f"  After reverse: {p}")
                    return p
                q.append(v)
    return []

ref_path = ref_bfs((0,0), (5,5))
print("\nFinal path:", ref_path)
print("Length:", len(ref_path))
