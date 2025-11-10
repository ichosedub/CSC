
import os
print("Current working directory:", os.getcwd())



from pathlib import Path


file_paths = [
    Path("pride_and_prejudice.txt"),
    Path("dracula.txt"),
    Path("moby_dick.txt")
]


for path in file_paths:
    try:
        text = path.read_text(encoding='utf-8').lower()
        total_the = text.count('the')
        spaced_the = text.count('the ')
        
        print(f"\n📘 {path.name}")
        print(f"Total 'the' count (approximate): {total_the}")
        print(f"'the ' count (more accurate): {spaced_the}")
    except Exception as e:
        print(f"Error reading {path.name}: {e}")

