import argparse

parser = argparse.ArgumentParser(description="-=== Command LIne Calculator ===-")

parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")

parser.add_argument("--add", action="store_true", help="For addition")
parser.add_argument("--sub", action="store_true", help="For subtraction")
parser.add_argument("--mul", action="store_true", help="For multiplication")
parser.add_argument("--div", action="store_true", help="For multiplication")

args = parser.parse_args()

if args.add:
    print("Addition Result:", args.num1 + args.num2)

elif args.sub:
    print("Subtraction Result:", args.num1 - args.num2)

elif args.mul:
    print("Multiplication Result:", args.num1 * args.num2)

elif args.div:
    print("Feature Comming soon!")

else:
    parser.print_help()

