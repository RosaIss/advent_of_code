"""--- Day 1: Report Repair ---"""

import sys

def sum2020():
    expenses = set()
    input_expenses = []    

    for line in sys.stdin:
        line = int(line[0:-1])
        input_expenses.append(line)
        expenses.add(line)

    for exp1 in input_expenses:
        exp2 = 2020 - exp1
        
        if exp2 in expenses:
            return exp1, exp2 

    return -1, -1
    
   
def main():
    exp1, exp2 = sum2020()
    
    if exp1 > 0:
        print("Exp1:{} Exp2:{} Multiplication:{}".
              format(exp1, exp2, exp1*exp2))
    else:
        print("Could not find two numbers that sum to 2020")
          

if __name__ == "__main__":
    main();


