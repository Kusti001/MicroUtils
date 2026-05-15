# TreePrint

A simple CLI tool that prints a directory tree structure.

## Clean mode

Removes common junk files like:

* __pycache__
* .pyc
* .DS_Store
* node_modules
* .git

Enable with:
`--clean` flag

## Usage

Run from terminal:

```bash
python3 path/treeprinter.py
```

```bash
python3 path/treeprinter.py --clean
```

## Ideas for improvement
* --depth limit
* --dirs-only