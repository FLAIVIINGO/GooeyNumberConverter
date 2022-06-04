import argparse, sys
from gooey import Gooey, GooeyParser

@Gooey(program_name='Number Converter',
    program_description='Enter a mathematic expression to translate output',
    clear_before_run='true')
def main():
  parser = GooeyParser(description='Number Converter')
  group = parser.add_mutually_exclusive_group(gooey_options={
      'initial_selection':0})
  group.add_argument(
      '-b',
      metavar='Convert to Binary',
      action='store',
      help='output to binary format')
  group.add_argument(
      '-o',
      metavar='Convert to Octal',
      action='store',
      help='output to octal format')
  group.add_argument(
      '-x',
      metavar='Convert to Hexadecimal',
      action='store',
      help='output to hexadecimal format')

  args = parser.parse_args()
  try:
    if args.b != None:
      result = eval(args.b)
      result = f'{int(result):#b}'
      res_arg = args.b
    elif args.o != None:
      result = eval(args.o)
      result = f'{int(result):#o}'
      res_arg = args.o
    elif args.x != None:
      result = eval(args.x)
      result = f'{int(result):#x}'
      res_arg = args.x

    print(f'{res_arg} = {result}')
  except (NameError, SyntaxError):
    sys.exit("Not a Valid Expression")

if __name__ == '__main__':
  main()
