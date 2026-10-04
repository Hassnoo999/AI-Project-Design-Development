"""Lab 01 Task 01: create the standard AI project folders safely."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOLDERS = ["data/raw", "data/processed", "models", "notebooks", "src", "configs", "logs"]


def main() -> None:
    for name in FOLDERS:
        folder = ROOT / name
        folder.mkdir(parents=True, exist_ok=True)
        (folder / ".gitkeep").touch(exist_ok=True)
    print("AI-Project-Design-Development/")
    for name in FOLDERS:
        print(f"  {name}/")
    print("  lab-01/   lab-02/   lab-03/")
    print("  .gitignore")
    print("Structure created successfully.")


if __name__ == "__main__":
    main()
