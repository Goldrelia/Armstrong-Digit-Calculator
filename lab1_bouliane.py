'''
Introduction to Computer Programming in Engineering and Science, 360-420-DW
Lab Assignment 1 - Aurelia Chu Bouliane ID: 2038264
'''
'''
Function 1:
(input) A function that receives one parameter called number.
(output) It returns a list that contains all the digits of number.
'''

# The function explode_number(number) seperates the input of number which is an integer into its digits.
# It then stores it into a list.
# This will be returned at the end.
# It uses mod 10 which allows for the extraction of the remainder.
# The floor operator allows for the access of the other numbers.
# This loops until the number seperates into all its digits.


def explode_number(number):
    digits = []
    while number > 0:
        digits.append(number % 10)
        number //= 10
    return digits


'''
Function 2:
(input) A function that receives one parameter called nber_digits.
(output) It returns a list of Armstrong numbers between start_number and 
end_number.
'''

# The function get_armstrong_numbers(nber_digits) loops through the number from a defined range.
# The range is given by the nber_digits input.
# Then it uses the explode_number function to help with calculations.
# It only keeps the ones that are Armstrong number.
# These numbers will be stored in a list and returned at the end


def get_armstrong_numbers(nber_digits):
    armstrong_nbers = []
    for i in range(10**(nber_digits - 1), 10**(nber_digits)):
        num_r = explode_number(i)
        sum_num = 0
        for j in num_r:
            sum_num += j**nber_digits
        if sum_num == i:
            armstrong_nbers.append(i)
    return armstrong_nbers


'''
Function 2:
(input) no parameter required
(output) no return required
'''

# The function main_program makes use of function get_armstrong_numbers.
# This allows to execute the whole program.
# It also uses a while loop which makes sure that we have a valid user input.


def main_program():
    print("Assignment prepared by Aurelia (2038264)")

    while True:
        digits = input("Please enter the number of digits [1,10]: ")

        if not digits.isnumeric():
            print("(invalid data)", end=" ")
            continue

        digits = int(digits)
        if digits < 1 or digits > 10:
            print("(invalid data)", end=" ")
            continue

        armstrongs = get_armstrong_numbers(digits)

        if len(armstrongs) == 0:
            print(f"There are no Armstrong number for {digits} digit nmbers")
        else:
            print(
                f"There are {len(armstrongs)} Armstrong numbers with {digits} digits"
            )
            print(armstrongs)
        break


main_program()
