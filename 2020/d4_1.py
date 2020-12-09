"""--- Day 4: Passport Processing ---"""

import sys


def validatePassport(passport, total_fields):
    count_fields = 0
    valid_fields = {"byr": 0, 
                    "iyr": 0,
                    "eyr": 0,
                    "hgt": 0,
                    "hcl": 0,
                    "ecl": 0,
                    "pid": 0,
                    "cid": 0 }    

    for line in passport:
        fields = line.split(" ")

        for field in fields:
            key, _ = field.split(":") 

            if key in valid_fields:
                #Do not accept duplicated fields
                if valid_fields[key] == 1:
                    return False
                else:
                    count_fields += 1
                    valid_fields[key] = 1

    if count_fields == total_fields:
        return True

    if count_fields == (total_fields - 1) and \
       valid_fields["cid"] == 0:
        return True

    return False 

    
def main():
    passport = []
    count_valid = 0

    for line in sys.stdin:
        line = line[:-1]

        if line == "":
            if validatePassport(passport, 8):
                count_valid += 1
            passport = []
        else:
            passport.append(line)
         
    if validatePassport(passport, 8):
        count_valid += 1

    print("Valid passports: {}".format(count_valid))


if "__main__" == __name__:
    main()
