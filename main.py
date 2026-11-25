#!/usr/bin/env python3
"""Write the tired dark lord monologue entry to /output/entry.txt."""
import os

TEXT = "Heroes. Sit. No, don't kneel \u2014 the floor is cold, and my knees ache just from watching you. Three hundred years I've held this mountain, and still you climb. You've come for the amulet. Third shelf of the left vault. The traps are mostly armed; I meant to reset them Tuesday, but the ravens needed feeding and these stairs... I built them young and dramatic. Now I dream of a chair with a back. Take the amulet. Take the crown too. Just close the door softly when you leave. The hinges scream, and I cannot bear one more scream today."

def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(tmp, 0o644)
    os.replace(tmp, "/output/entry.txt")

if __name__ == "__main__":
    main()
