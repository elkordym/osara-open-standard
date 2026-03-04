from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "specs"
TARGET_DIR = ROOT / "docs" / "specs"
ASSETS_SOURCE_DIR = ROOT / "assets" / "diagrams"
ASSETS_TARGET_DIR = ROOT / "docs" / "assets" / "diagrams"


def main() -> None:
    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    for src in SOURCE_DIR.glob("*-draft.md"):
        dst = TARGET_DIR / src.name
        shutil.copy2(src, dst)
        print(f"synced {src.name} -> docs/specs/")

    ASSETS_TARGET_DIR.mkdir(parents=True, exist_ok=True)
    for src in ASSETS_SOURCE_DIR.glob("*"):
        if src.is_file():
            dst = ASSETS_TARGET_DIR / src.name
            shutil.copy2(src, dst)
            print(f"synced {src.name} -> docs/assets/diagrams/")


if __name__ == "__main__":
    main()
