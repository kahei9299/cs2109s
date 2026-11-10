import os, sys
sys.path.insert(0, os.path.dirname(__file__))
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from pathlib import Path
import numpy as np
from PIL import Image
from sklearn.linear_model import LogisticRegression
from grid_adventure.rendering import DEFAULT_ASSET_ROOT
from utils import generate_sklearn_loader_snippet

CELL_SIZE = 32
root = Path(DEFAULT_ASSET_ROOT)

ENTITY_DIRS = {
    "wall": 1, "human": 2, "coin": 3, "gem": 4, "box": 5,
    "key": 6, "locked": 7, "opened": 8, "shield": 9,
    "ghost": 10, "boots": 11, "lava": 12, "exit": 13,
}

floor_dir = root / "floor"
floor_files = sorted(f for f in floor_dir.iterdir() if f.suffix == '.png')
floor_imgs = []
for f in floor_files:
    with Image.open(f) as im:
        floor_imgs.append(im.convert("RGBA").resize((CELL_SIZE, CELL_SIZE)))
print(f"Loaded {len(floor_imgs)} floor variants")

X_data = []
y_data = []

for floor in floor_imgs:
    arr = np.asarray(floor)[:, :, :3].flatten().astype(np.float32) / 255.0
    X_data.append(arr)
    y_data.append(0)

for dirname, label in ENTITY_DIRS.items():
    ent_dir = root / dirname
    ent_files = sorted(f for f in ent_dir.iterdir() if f.suffix == '.png')
    count = 0
    for ef in ent_files:
        with Image.open(ef) as im:
            ent_img = im.convert("RGBA").resize((CELL_SIZE, CELL_SIZE))
        for floor in floor_imgs:
            comp = Image.alpha_composite(floor, ent_img)
            arr = np.asarray(comp)[:, :, :3].flatten().astype(np.float32) / 255.0
            X_data.append(arr)
            y_data.append(label)
            count += 1
    print(f"  {dirname}: {count} composites (label {label})")

X = np.array(X_data)
y = np.array(y_data)
print(f"\nTraining data: {X.shape[0]} samples, {X.shape[1]} features, {len(set(y))} classes")

print("\nTraining LogisticRegression...")
model = LogisticRegression(max_iter=2000, C=1.0, solver='lbfgs', n_jobs=1)
model.fit(X, y)

train_acc = model.score(X, y)
print(f"Training accuracy: {train_acc:.4f}")

snippet = generate_sklearn_loader_snippet(model, compression="zlib")
with open(os.path.join(os.path.dirname(__file__), "model_snippet.py"), "w") as f:
    f.write(snippet)
print(f"\nSnippet saved to model_snippet.py ({len(snippet)} chars, ~{len(snippet)//1024}KB)")
