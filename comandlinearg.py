import argparse
parser=argparse.ArgumentParser(description="salary caluculaator CLI Tool")
#reading the arguments
parser.add_argument("name",help="employee name")
parser.add_argument("basic",help="employee basic",type=int)
parser.add_argument("bonus",help="employee bonus in percentage",type=int)
parser.add_argument("tax",help="employee tax in percentage",type=int)

#Optional flags
parser.add_argument("--gross",action="store_true",help="Show grass salary ")
parser.add_argument("--net",action="store_true",help="Show net salary ")
parser.add_argument("--all",action="store_true",help="Show complete report ")

args= parser.parse_args()

#calucualtion logic

bonus_amount=(args.bonus / 100) *args.basic
tax_amount=(args.tax / 100) * args.basic
gross_salary=args.basic + bonus_amount
net_salary=gross_salary - tax_amount

if args.all:
    print("\n SALARY FULL REPORT")
    print("\-------------")
    print("Employee name: ",args.name)
    print("Basic Salary :",args.basic)
    print("Bonus Amount :",bonus_amount)
    print("Tax Amount :",tax_amount)
    print("Gross Salary :",gross_salary,)
    print("Net Salary :",net_salary,)
else:
    if args.gross:
        print("Gross salary :",gross_salary)
    if args.net:
        print("Net Salary :",net_salary,)
    if not ( args.gross or args.net):
        parser.print_help()
