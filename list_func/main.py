import argparse

from process import walk

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="list function/method in modules")
    parser.add_argument('--dir')
    parser.add_argument('--module')
    args = parser.parse_args()
    if not args.dir:
        print(' '.join(walk('./', str(args.module))))
    else:
        print(' '.join(walk(str(args.dir), str(args.module))))
