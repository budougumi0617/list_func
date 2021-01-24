from ast import parse, dump, ClassDef, FunctionDef


def process(src: str) -> list[str]:
    results: list[str] = []
    got = parse(src)
    print(dump(got, indent=4))
    for node in got.body:
        if isinstance(node, FunctionDef):
            results.append(node.name)
        elif isinstance(node, ClassDef):
            for cnode in node.body:
                if isinstance(cnode, FunctionDef):
                    results.append(f'{node.name}.{cnode.name}')

    return results
