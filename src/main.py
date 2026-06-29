from pathlib import Path

from parser.ts_parser import parse_typescript

from discovery.finder import discover_files

from extractor.class_extractor import walk_tree


project = Path("samples")

files = discover_files(project)

print("Discovered files:")

for file in files:
    print(file)

source = Path("samples/sample.ts").read_text(encoding="utf8")

tree = parse_typescript(source)

print("Parsing Successful!")



walk_tree(tree.root_node)



