import os
from ast import parse, dump, ClassDef, FunctionDef


def process(src: str) -> list[str]:
    results: list[str] = []
    got = parse(src)
    # print(dump(got, indent=4))
    for node in got.body:
        if isinstance(node, FunctionDef):
            results.append(node.name)
        elif isinstance(node, ClassDef):
            for cnode in node.body:
                if isinstance(cnode, FunctionDef):
                    results.append(f'{node.name}.{cnode.name}')

    return results


def walk(root: str) -> list[str]:
    results: list[str] = []
    for cur_dir, dirs, files in os.walk(root):
        for file in files:
            _, ext = os.path.splitext(file)
            if not file.startswith('test_') and ext == '.py':
                file_path = os.path.join(cur_dir, file)
                module_path = file_path.replace(root, '').replace('/', '.').removeprefix('.').removesuffix('.py')
                with open(file_path, encoding='utf-8') as f:
                    results.extend([f'{module_path}:{s}' for s in process(f.read())])
    return results
