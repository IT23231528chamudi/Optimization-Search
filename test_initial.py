from student_sa import _bfs_path
import json

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

path = _bfs_path((0,0), (5,5), neighbors_fn)
print('BFS Path:', path)
print('Length:', len(path))

def count_turns(p):
    if len(p) < 3:
        return 0
    turns = 0
    for i in range(2, len(p)):
        dir1 = (p[i-1][0] - p[i-2][0], p[i-1][1] - p[i-2][1])
        dir2 = (p[i][0] - p[i-1][0], p[i][1] - p[i-1][1])
        if dir1 != dir2:
            turns += 1
    return turns

turns = count_turns(path)
cost = len(path) + 0.2 * turns
print('Turns:', turns)
print('Cost:', cost)
