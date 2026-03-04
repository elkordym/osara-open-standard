from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "specs"
TARGET_DIR = ROOT / "docs" / "specs"


def main() -> None:
    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    for src in SOURCE_DIR.glob("*-draft.md"):
        dst = TARGET_DIR / src.name
        shutil.copy2(src, dst)
        print(f"synced {src.name} -> docs/specs/")


if __name__ == "__main__":
    main()
