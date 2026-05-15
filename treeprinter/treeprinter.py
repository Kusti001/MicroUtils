import pathlib
import argparse

TRASH_NAMES = {
    "__pycache__",
    ".DS_Store",
    "node_modules",
    ".git",
}

def print_tree(path='.', prefix='', clean=False):
    """
    Recursively prints the directory tree.
    path: current folder ('.' = here)
    prefix: indentation for branches
    """
    try:
        items = [item for item in pathlib.Path(path).iterdir() if (not clean or item.name not in TRASH_NAMES)]  #take items in the directory
        items.sort(key=lambda x: (not x.is_dir(), x.name.lower()))  #sort by type and name

        for i, item in enumerate(items):  #loop through items
            is_dir = item.is_dir()  #is file folder?
            is_last = i == len(items) - 1 #is it the last item?

            if is_last:
                if is_dir:
                    marker = '└── 📁 '
                else:
                    marker = '└── 📄 '
            else:
                if is_dir:
                    marker = '├── 📁 '
                else:
                    marker = '├── 📄 '

            print(f"{prefix}{marker}{item.name}") #print the item with the correct marker

            if is_dir:  #if it's a directory, we need to go deeper
                new_prefix = prefix + ('    ' if is_last else '│   ')  #update the prefix for the next level
                print_tree(item, new_prefix)  #recursive call for directories

    except PermissionError:
        print(f"{prefix}├── [no access]")
    except Exception as e:
        print(f"{prefix}├── [Error: {e}]")

if __name__ == "__main__":
    
    print(f"📁 {pathlib.Path().resolve().name}")

    parser = argparse.ArgumentParser()
    parser.add_argument("--clean", action="store_true")
    args = parser.parse_args()

    print_tree(clean=args.clean)
    print("\n\033[34mThanks for using this tool!\033[38;5;229m >_<\033[0m")