import sys, os, time, json, types
sys.path.insert(0, os.path.dirname(__file__))
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from utils import evaluate_level, get_minimum_total_reward
from public_levels.catalog import (
    PUBLIC_BOSS_LEVEL_BUILDERS, PUBLIC_LEVEL_MAX_REWARDS,
    PUBLIC_TURN_LIMIT, PUBLIC_BOSS_TIME_LIMIT,
)

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

print(f"{'Level':<45} {'Type':<8} {'Score':>7} {'Optimal':>8} {'Perf':>6} {'Win':>4} {'Time':>6}")
print("-" * 90)

for obs_type in ("gridstate", "image"):
    for name in sorted(PUBLIC_BOSS_LEVEL_BUILDERS.keys()):
        builder = PUBLIC_BOSS_LEVEL_BUILDERS[name]
        optimal = PUBLIC_LEVEL_MAX_REWARDS[name]
        min_r = get_minimum_total_reward(builder)
        result = evaluate_level(
            Agent, builder,
            max_total_reward=optimal, min_total_reward=min_r,
            observation_type=obs_type,
            time_limit=PUBLIC_BOSS_TIME_LIMIT,
            turn_limit=PUBLIC_TURN_LIMIT,
        )
        perf = result["performance"]
        win = result["win"]
        score = result["total_reward"]
        rt = result["runtime (sec)"]
        status = "OK" if win else "FAIL"
        label = f"{name} ({obs_type})"
        print(f"{label:<45} {obs_type:<8} {score:>7} {optimal:>8} {perf:>6.3f} {status:>4} {rt:>5.1f}s")

print("-" * 90)
