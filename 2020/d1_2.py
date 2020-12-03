"""--- Day 1: Report Repair - part 2 ---"""

import sys

def parse_input(input_expenses, expenses):
    for line in sys.stdin:
        line = int(line[0:-1])
        input_expenses.append(line)
        expenses.add(line)
    

def sum2020(input_expenses, expenses, sum_exp):
    for exp1 in input_expenses:
        exp2 = sum_exp - exp1
        
        if exp2 in expenses and exp1 != exp2 and \
           exp1 != sum_exp and exp2 != sum_exp:
            return exp1, exp2 

    return -1, -1
    
   
def main():
    expenses = set()
    input_expenses = []
    exp1 = -1
    exp2 = -1

    parse_input(input_expenses, expenses)
    
    for exp3 in input_expenses:
        sum_exp = 2020 - exp3

        exp1, exp2 = sum2020(input_expenses, expenses,
                             sum_exp)
        
        if exp1 > 0:
            break
    
    if exp1 > 0:
        print("Exp1:{} Exp2:{} Exp3:{} "
              "Multiplication:{}".
              format(exp1, exp2, exp3, exp1*exp2*exp3))
    else:
        print("Could not find trhee numbers that sum to 2020")
          

if __name__ == "__main__":
    main();


