from gooey import Gooey, GooeyParser
import argparse, sys

@Gooey()
def main():
  parser = GooeyParser(description='Enter an expression to be evaluated.')

#group = parser.add_mutually_exclusive_group(required=True, 
#gooey_options={'initial_selection':0})

  parser.add_argument(
      'ip_expr',
      metavar='Expression Field',
      help='Enter some text')
  
  parser.add_argument(
      '-b',
      metavar='Binary Converter',
      action='store_true',
      help='output in binary format')
  parser.add_argument(
      '-o',
      metavar='Octal Converter',
      action='store_true',
      help='output in octal format')
  
  parser.add_argument(
      '-x',
      metavar='Hexadecimal Converter',
      action='store_true',
      help='output in hexadecimal format')
  

  args = parser.parse_args()
  print(args.b)
  try:
    result = eval(args.ip_expr)
    if args.b:
      result = f'{int(result):#b}'
    elif args.o:
      result = f'{int(result):#o}'
    elif args.x:
      result = f'{int(result):#x}'

    print(f'{args.ip_expr} = {result}')
  except (NameError, SyntaxError):
    sys.exit("Not a Valid Expression")

if __name__ == '__main__':
  main()
