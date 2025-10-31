import json
from collections import deque

# Load problem
data = json.load(open('problem.json'))
obstacles = set(tuple(o) for o in data['obstacles'])
print("Obstacles:", obstacles)

def neighbors_fn(u):
    r, c = u
    out = []
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 6 and 0 <= nc < 6 and (nr, nc) not in obstacles:
            out.append((nr, nc))
    return out

# Reference BFS (from runner)
def ref_bfs(start, goal):
    if start == goal: return [start]
    q = deque([start])
    parent = {start: None}
    while q:
        u = q.popleft()
        for v in neighbors_fn(u):
            if v not in parent:
                parent[v] = u
                if v == goal:
                    p = [v]
                    while parent[p[-1]] is not None:
                        p.append(parent[p[-1]])
                    p.append(start)
                    p.reverse()
                    return p
                q.append(v)
    return []

# Student BFS
def student_bfs(start, goal):
    if start == goal:
        return [start]
    queue = deque([start])
    parent = {start: None}
    while queue:
        u = queue.popleft()
        if u == goal:
            path = []
            cur = u
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            path.reverse()
            return path
        for v in neighbors_fn(u):
            if v not in parent:
                parent[v] = u
                queue.append(v)
    return []

ref_path = ref_bfs((0,0), (5,5))
student_path = student_bfs((0,0), (5,5))

print("\nReference BFS path:", ref_path)
print("Length:", len(ref_path))
print("\nStudent BFS path:", student_path)
print("Length:", len(student_path))
print("\nMatch:", ref_path == student_path)
