from src.parser.ts_parser import parse_typescript
from src.extractor.class_extractor import ClassExtractor
from src.tree.Walker import walk


with open(
    "samples/sample.ts",
    "r",
    encoding="utf-8"
) as file:

    source = file.read()


tree = parse_typescript(source)

extractor = ClassExtractor()

walk(
    tree.root_node,
    extractor.visit
)

print(extractor.classes)