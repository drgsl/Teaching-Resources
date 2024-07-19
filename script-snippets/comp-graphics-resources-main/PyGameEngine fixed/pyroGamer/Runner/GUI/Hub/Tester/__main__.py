
import sys
import argparse


parser = argparse.ArgumentParser(description='Hub Utility')
parser.add_argument('--Test', action='store_true')


args = parser.parse_args()

print("init")

if args.Test:
    print("Test")
else:
    print("No Test")

print('Hello world', file=sys. stderr)