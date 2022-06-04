import argparse, sys
from math import *



parser = argparse.ArgumentParser()
parser.add_argument('ip_expr',
    help="Input Expression to be Evaluated")
parser.add_argument('-f', type=int,
    help="Specify Floating Point Output Precision")
parser.add_argument('-F', action="store_true",
    help="No Floating Point Output Precision")

args = parser.parse_args()

try:
  flag = False
  result = eval(args.ip_expr)
  if args.f:
    result = f'{result:.{args.f}f}'
  elif type(result) == float:
    if args.F:
      print(result)
      flag = True
    else:
      result = f'{result:.2f}'
  if flag == False:
    print(result)
except (NameError, SyntaxError):
  sys.exit("Error: Not a Valid Expression")
