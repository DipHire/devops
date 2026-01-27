import sys

# print("Script name:", sys.argv[0])
# print("First argument:", sys.argv[1])
# print("Second argument:", sys.argv[2])


# a = int(sys.argv[1])
# b = int(sys.argv[2])

# print("Sum =", a + b)

# print( sys.argv[1] + sys.argv[2])


# if len(sys.argv) != 3:
#     print("Usage: python add.py num1 num2")
# else:
#     a = int(sys.argv[1])
#     b = int(sys.argv[2])
#     print("Sum =", a + b)


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("num1", type=int)
parser.add_argument("num2", type=int)

args = parser.parse_args()

print("Sum =", args.num1 + args.num2)

    