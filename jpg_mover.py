"""Move all .jpg files from one folder into a new folder.

CodeAlpha Python Programming Internship.
"""

import argparse
import shutil
from pathlib import Path

JPG_EXTENSIONS = {".jpg", ".jpeg"}


def move_jpgs(source, destination):
    """Move all .jpg/.jpeg files from source to destination. Returns moved file names."""
    source = Path(source)
    destination = Path(destination)
    if not source.is_dir():
        raise FileNotFoundError("Source folder not found: " + str(source))
    destination.mkdir(parents=True, exist_ok=True)

    moved = []
    for file in source.iterdir():
        if file.is_file() and file.suffix.lower() in JPG_EXTENSIONS:
            target = destination / file.name
            counter = 1
            while target.exists():
                target = destination / (file.stem + "_" + str(counter) + file.suffix)
                counter += 1
            shutil.move(str(file), str(target))
            moved.append(target.name)
    return sorted(moved)


def main():
    parser = argparse.ArgumentParser(description="Move all .jpg files into a new folder.")
    parser.add_argument("source", help="Folder to scan")
    parser.add_argument("destination", help="Folder to move the images into")
    args = parser.parse_args()

    try:
        moved = move_jpgs(args.source, args.destination)
    except FileNotFoundError as error:
        print("Error:", error)
        return
    print("Moved " + str(len(moved)) + " file(s) to " + args.destination)


if __name__ == "__main__":
    main()
