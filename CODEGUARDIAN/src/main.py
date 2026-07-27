from pathlib import Path

from CODEGUARDIAN.src.parser.ts_parser import parse_typescript

from CODEGUARDIAN.src.discovery.finder import discover_files

from CODEGUARDIAN.src.extractor.class_extractor import ClassExtractor

from CODEGUARDIAN.src.extractor.import_extractor import importExtractor

from CODEGUARDIAN.src.extractor.function_extractor import functionExtractor
from CODEGUARDIAN.src.tree.Walker import walk



project = Path("")


files = discover_files(
    project,
    {".ts", ".js",}
)

print("Discovered files:")

for file in files:
    print(file)
    source = file.read_text(encoding="utf8")  

    tree = parse_typescript(source)



    extractor = ClassExtractor()

    walk(tree.root_node, extractor.visit)

    print(extractor.classes)


    extractor = functionExtractor()

    walk(tree.root_node, extractor.visit)

    print(extractor.function)

    extractor = importExtractor()
 
    walk(tree.root_node, extractor.visit)
    print(extractor.imports)





"""classes = []
extract_classes(tree.root_node, classes)

print("\nClasses Found:")

for class_name in classes:
    print(f"- {class_name}")
"""


