import argparse

from list_func.process import walk

def main():
    parser = argparse.ArgumentParser(description="list function/method in modules")
    parser.add_argument('--dir')
    parser.add_argument('--module')
    args = parser.parse_args()
    if not args.dir:
        print(' '.join(walk('./', str(args.module))))
    else:
        print(' '.join(walk(str(args.dir), str(args.module))))


if __name__ == '__main__':
    main()