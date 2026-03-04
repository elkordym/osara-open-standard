from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "specs"
TARGET_DIR = ROOT / "docs" / "specs"
ASSETS_SOURCE_DIR = ROOT / "assets" / "diagrams"
ASSETS_TARGET_DIR = ROOT / "docs" / "assets" / "diagrams"


def main() -> None:
    if TARGET_DIR.exists():
        shutil.rmtree(TARGET_DIR)
    shutil.copytree(SOURCE_DIR, TARGET_DIR)
    print("synced specs tree -> docs/specs/")

    ASSETS_TARGET_DIR.mkdir(parents=True, exist_ok=True)
    for src in ASSETS_SOURCE_DIR.glob("*"):
        if src.is_file():
            dst = ASSETS_TARGET_DIR / src.name
            shutil.copy2(src, dst)
            print(f"synced {src.name} -> docs/assets/diagrams/")


if __name__ == "__main__":
    main()
