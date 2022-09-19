# # Problem 26: Reciprocal cycles
# A unit fraction contains 1 in the numerator. The decimal representation of the unit
# fractions with denominators 2 to 10 are given:
#     1/2	= 	0.5
#     1/3	= 	0.(3)
#     1/4	= 	0.25
#     1/5	= 	0.2
#     1/6	= 	0.1(6)
#     1/7	= 	0.(142857)
#     1/8	= 	0.125
#     1/9	= 	0.(1)
#     1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring
# cycle. Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


def divide(dividend, divisor, decimal_places):
    """
    This function find the decimal approximation of the dividing any two numbers
    An easier method would be to use this package to find it and to specify the precision
    from decimal import *
    getcontext().prec = 50
    answer = Decimal(1)/Decimal(7)
    """
    dividend = str(dividend)
    length = len(dividend)
    right_dec = left_dec = ''

    # for loop for length of 'a' and stop if found answer for dividend ÷ b
    for i in range(1, length + 2):
        (quo, mod) = divmod(int(dividend[:i]), divisor)  # finds the quotient and modulus (remainder)

        if 0 == int(dividend):  # if value is zero, break
            left_dec = left_dec + '0' * (len(dividend) - len(left_dec))
            # print('exact value found')
            break
        if int(dividend) < divisor:  # if remainder remains after division, break
            # print('non-integer solution')
            break

        # save value to running value (dividend) and save quotient to list
        left_dec += str(quo)
        dividend = str(str(mod) + dividend[i:]).zfill(length)

    if int(dividend) < divisor:  # criteria for second loop to find decimal values
        for i in range(length + 1, decimal_places + length + 1):
            dividend = dividend + '0'
            (quo, mod) = divmod(int(dividend), divisor)  # finds the quotient and modulus (remainder)

            if 0 == int(dividend):  # if value is zero, break
                right_dec = right_dec + '0' * (len(dividend) - len(right_dec))
                # print('exact value found')
                break

            # save value to running value (dividend) and save quotient to list
            right_dec += str(quo)
            dividend = str(str(mod) + dividend[i:]).zfill(length)

    answer_str = left_dec + '.' + right_dec
    answer_flo = float(answer_str)
    # print(f'(answer_str, answer_float) = \n {(answer_str, answer_flo)}')
    return answer_str, answer_flo


# take the second to last digit just in case there is any rounding applied to number
def reciprocal(str_in: str):
    """
    test if the number next to it is identical
    then test 3 sets of 2 numbers
    then test 3 sets of 3 numbers and so on
    """
    n = 0
    if len(string) < 6:
        n = 0
        return n
    else:
        for i in range(1, len(str_in) // 2):
            string_ref = str_in[len(str_in) - i - 1: len(str_in) - 1]
            string_test_1 = str_in[len(str_in) - 2 * i - 1: len(str_in) - i - 1]
            string_test_2 = str_in[len(str_in) - 3 * i - 1: len(str_in) - 2 * i - 1]
            # print(string_ref, string_test_1, string_test_2)
            if string_test_1 == string_test_2 == string_ref:
                # print('it has a reciprocal of', i + 1)
                n = i
                break
            else:
                n = 0
    return n


a = 1
# b, the divisor which is defined in for function
c = 3000  # decimal places
cycles = x = 0  # preallocation

for b in range(2, 1000):  # test values from 1/2 to 1/999
    string, flo = divide(a, b, c)
    test_cyc = reciprocal(string)
    print(f'1/{b} = {flo} and has {test_cyc} reciprocal cycles')

    if cycles < test_cyc:  # find largest value
        cycles, x = (test_cyc, b)

# print answer
print(f'{x} has the largest reciprocal cycle at {cycles} digits long')
