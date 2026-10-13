from pathlib import Path
import ast
import sys

root = Path(__file__).resolve().parents[1]
backend = root / "backend"
errors = []
for path in backend.rglob("*.py"):
    try:
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except SyntaxError as exc:
        errors.append(f"{path}: {exc}")
required = [
    "README.md", "backend/app/main.py", "backend/requirements.txt",
    "frontend/package.json", "frontend/src/App.tsx", "frontend/src/api.ts"
]
for rel in required:
    if not (root / rel).is_file():
        errors.append(f"Missing required file: {rel}")
if errors:
    print("Project verification failed:")
    print("\n".join(errors))
    sys.exit(1)
print(f"Static file check passed. Parsed {len(list(backend.rglob('*.py')))} Python files.")
print("Dependency installation and frontend build still need to be run on the target machine.")
