""" Day 1: Inverse Captcha part 1 """

def captcha(numbers):
    total = 0
    it = iter(numbers[:-1])
    for number in numbers[1:]:
        if number == it.next():
            total += int(number)
    
    if numbers[0] == numbers[-1]:
        total += int(number[0])
    return total
             
 
seq = raw_input()
print captcha(seq)
