from CODEGUARDIAN.src.parser.ts_parser import (
    parse_typescript
)


with open(
    "samples/sample.ts",
    "r",
    encoding="utf-8"
) as file:

    source = file.read()


tree = parse_typescript(source)

print(tree.root_node)