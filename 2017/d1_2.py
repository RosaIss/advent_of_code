""" Day 1: Inverse Captcha part 2 """

def captcha(numbers):
    total = 0
    half = (len(numbers) / 2)
    it = iter(numbers[:-half])
    for number in numbers[half:]:
        if number == it.next():
            total += int(number)
    return total * 2
             
 
seq = raw_input()
print captcha(seq)
