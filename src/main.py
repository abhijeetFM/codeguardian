from pathlib import Path

from parser.ts_parser import parse_typescript

from discovery.finder import discover_files

from extractor.class_extractor import ClassExtractor

from extractor.function_extractor import functionExtractor
from src.tree.Walker import walk


project = Path("samples")

files = discover_files(project)

print("Discovered files:")

for file in files:
    print(file)

source = Path("samples/sample.ts").read_text(encoding="utf8")

tree = parse_typescript(source)

print("Parsing Successful!")

extractor = ClassExtractor()

walk(tree.root_node, extractor.visit)

print(extractor.classes)


extractor = functionExtractor()

walk(tree.root_node, extractor.visit)

print(extractor.function)





"""classes = []
extract_classes(tree.root_node, classes)

print("\nClasses Found:")

for class_name in classes:
    print(f"- {class_name}")
"""


