import sys
from pathlib import path
import argparse


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  subparsers = parser.add_subparsers(dest='command', required = True)
  
  parser_base = subparsers.add_parser('base')
  parser_base.set_defaults(func=hello_world)

  
  args = parser.parse_args()
  
  args.func(args)
  
