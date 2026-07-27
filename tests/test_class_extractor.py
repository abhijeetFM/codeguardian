from CODEGUARDIAN.src.parser.ts_parser import parse_typescript
from CODEGUARDIAN.src.extractor.class_extractor import ClassExtractor
from CODEGUARDIAN.src.tree.Walker import walk


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