import sys
from pathlib import path
import argparse


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  subparsers = pareser.add_subparsers(dest='command', required = True)
  
  parser_base = subparsers.add_parser('base')
  parser_base.add_argument('--debug')
  
  args = parser.parse_args()
  
  args.func(args)
  
