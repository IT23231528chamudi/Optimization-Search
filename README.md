# Optimization-Search

Implementations and experiments for search and optimization algorithms used for coursework and research (BFS, IDS, A*, simulated annealing, LP/DP for knapsack, etc.). This repository contains algorithm implementations, runners, example problem files, and result/metrics logging.

## Table of contents
- About
- Requirements
- Installation
- Usage
- Project layout
- Running tests
- Configuration
- Contributing
- License

## About

This repo collects several classical search and optimization algorithm implementations along with small runners and utilities to run experiments and collect results. It's intended for education, experiments, and benchmarking heuristics.

## Requirements

- Python 3.8+ (adjust if you use another interpreter)
- Standard library only unless you add external dependencies (see `requirements.txt` if present)

Optional tools
- `pytest` for running tests (if added)

## Installation

Clone the repo and (optionally) create a virtual environment:

```powershell
git clone <repo-url>
cd Optimization-Search
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If a `requirements.txt` is present, install dependencies with:

```powershell
pip install -r requirements.txt
```

## Usage

Run the main experiment runners or individual algorithm scripts. Examples below use PowerShell on Windows.

- Run the default experiment runner:

```powershell
python .\runner.py
```

- Run the MSc runner (alternate experiment harness):

```powershell
python .\runner_Msc.py
```

- Run individual algorithm scripts:

```powershell
python .\student_bfs.py
python .\student_astar.py
python .\student_ids.py
python .\student_sa.py
python .\student_lp_dp.py
```

Runners and scripts typically read input from `problem.json` and write outputs into `results/` and `results.json`.

## Project layout

- `common.py` — shared helpers and utilities
- `heuristics.py` — heuristic functions used by A* and experiments
- `student_bfs.py`, `student_astar.py`, `student_ids.py`, `student_sa.py`, `student_lp_dp.py` — algorithm implementations
- `runner.py`, `runner_Msc.py` — experiment runners that orchestrate runs and write results
- `test_initial.py` — small sanity tests / smoke tests
- `problem.json` — sample problem input(s)
- `results/` — produced metrics and result files (e.g. `search_metrics.json`, `knapsack_result.json`)
- `index.html` — optional visualization/summary page
- `trace_ref.py`, `debug_bfs.py` — tracing and debug helpers

## Running tests

If the project includes tests you can run the basic test file directly:

```powershell
python .\test_initial.py
```

If you add pytest to the project, run:

```powershell
pip install pytest
pytest -q
```

## Configuration and inputs

- Edit `problem.json` to change the input instance(s) used by the runners.
- Runners write outputs to `results/` and `results.json`. Add these files to `.gitignore` if you don't want to track generated outputs.

## Contributing

If you'd like to contribute:

1. Fork the repository
2. Create a feature branch: `feature/your-change`
3. Add tests for any new behavior
4. Open a pull request with a clear description

## License

Add your license of choice here (for example, `MIT`). If you don't want to open-source the project, replace this with your copyright statement.

## Contact

Add maintainer/author contact info here (name, email, affiliation).

---

If you'd like I can:
- add a `requirements.txt` listing non-stdlib dependencies,
- add a GitHub Actions workflow to run the tests on push/PR,
- add badges and a short demo section with sample outputs.
