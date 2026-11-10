"""Assemble cell_code_prefix.py + model_snippet.py + cell_code_suffix.py
into notebook cell 5efe1171."""
import json, os

base = os.path.dirname(__file__)
nb_path = os.path.join(base, "capstone-project.ipynb")

with open(os.path.join(base, "cell_code_prefix.py")) as f:
    prefix = f.read()
with open(os.path.join(base, "model_snippet.py")) as f:
    snippet = f.read()
with open(os.path.join(base, "cell_code_suffix.py")) as f:
    suffix = f.read()

full_source = prefix + snippet + "\n" + suffix

with open(nb_path) as f:
    nb = json.load(f)

found = False
for cell in nb["cells"]:
    if cell.get("id") == "5efe1171" and cell["cell_type"] == "code":
        cell["source"] = full_source.split("\n")
        cell["source"] = [line + "\n" for line in cell["source"][:-1]] + [cell["source"][-1]]
        cell["outputs"] = []
        cell["execution_count"] = None
        found = True
        break

if not found:
    print("ERROR: cell 5efe1171 not found")
    exit(1)

with open(nb_path, "w") as f:
    json.dump(nb, f, indent=1)

total_chars = len(full_source)
print(f"Cell updated: {total_chars} chars ({total_chars / 1024:.1f} KB)")
print(f"Notebook written: {nb_path}")
