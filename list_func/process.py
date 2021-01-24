from ast import parse, dump


def process(src: str) -> list[str]:
    got = parse(src)
    print(dump(got, indent=4))
    return []
