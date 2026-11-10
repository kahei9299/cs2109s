import sys, os, time, json, types
sys.path.insert(0, os.path.dirname(__file__))
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from utils import evaluate_level, get_minimum_total_reward
from public_levels.catalog import (
    PUBLIC_GAMEPLAY_LEVEL_BUILDERS, PUBLIC_LEVEL_MAX_REWARDS,
    PUBLIC_TURN_LIMIT, PUBLIC_GAMEPLAY_TIME_LIMIT,
)

# Load agent code from notebook cell
nb_path = os.path.join(os.path.dirname(__file__), "capstone-project.ipynb")
with open(nb_path) as f:
    nb = json.load(f)
agent_code = None
for cell in nb["cells"]:
    if cell.get("id") == "5efe1171" and cell["cell_type"] == "code":
        agent_code = "".join(cell["source"]); break
if agent_code is None:
    print("ERROR: Could not find cell 5efe1171"); sys.exit(1)

agent_mod = types.ModuleType("agent_mod")
agent_mod.__file__ = nb_path
sys.modules["agent_mod"] = agent_mod
exec(compile(agent_code, nb_path, "exec"), agent_mod.__dict__)
Agent = agent_mod.Agent

print(f"{'Level':<40} {'Score':>7} {'Optimal':>8} {'Perf':>6} {'Win':>4} {'Time':>6}")
print("-" * 75)

total_levels = 0; passed = 0; all_win = True

for name in sorted(PUBLIC_GAMEPLAY_LEVEL_BUILDERS.keys()):
    builder = PUBLIC_GAMEPLAY_LEVEL_BUILDERS[name]
    optimal = PUBLIC_LEVEL_MAX_REWARDS[name]
    min_r = get_minimum_total_reward(builder)
    result = evaluate_level(
        Agent, builder,
        max_total_reward=optimal, min_total_reward=min_r,
        observation_type="gridstate",
        time_limit=PUBLIC_GAMEPLAY_TIME_LIMIT,
        turn_limit=PUBLIC_TURN_LIMIT,
    )
    perf = result["performance"]
    win = result["win"]
    score = result["total_reward"]
    rt = result["runtime (sec)"]
    status = "OK" if win else "FAIL"
    total_levels += 1
    if win and perf >= 0.85: passed += 1
    if not win: all_win = False
    print(f"{name:<40} {score:>7} {optimal:>8} {perf:>6.3f} {status:>4} {rt:>5.1f}s")

print("-" * 75)
print(f"Passed (win + perf>=0.85): {passed}/{total_levels}")
if all_win:
    print("All levels WON!")
else:
    print("Some levels FAILED")
