from src.parser.ts_parser import parse_typescript
from src.extractor.function_extractor import (
    functionExtractor
)
from src.tree.Walker import walk


with open(
    "samples/sample.ts",
    "r",
    encoding="utf-8"
) as file:

    source = file.read()


tree = parse_typescript(source)

extractor = functionExtractor()

walk(
    tree.root_node,
    extractor.visit
)

print(extractor.function)