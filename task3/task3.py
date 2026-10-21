import sys
from pathlib import Path
from colorama import Fore

def print_dir_structure():
    try:
        dir_path = sys.argv[1]
    except IndexError:
        print('Directory was not provided')
        return
    
    root = Path(dir_path).resolve()
    
    if not root.exists():
        print("Path does not exist")
        return

    if not root.is_dir():
        print("Path is not a directory")
        return
    
    print(f"{Fore.GREEN}{root.name}/")

    def iterate_dir(dir_pathname, prefix = ""):
        root = Path(dir_pathname)
        entries = sorted(root.iterdir())

        for index, entry in enumerate(entries):
            is_last = index == len(entries) - 1
            branch = Fore.YELLOW + ("└── " if is_last else "├── ")
            is_dir = entry.is_dir()
            name = f"{Fore.GREEN}{entry.name}/" if is_dir else f"{Fore.BLUE}{entry.name}"
            print(prefix + branch + name)

            if is_dir:
                next_prefix = Fore.YELLOW + prefix + ("    " if is_last else "│   ")
                iterate_dir(entry, next_prefix)

    iterate_dir(dir_path)

print_dir_structure()

# python3 task3.py test_dir