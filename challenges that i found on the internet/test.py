"""Test the challenges"""
import math
import sort_a_list
import radian_to_degree
import count_vowels
import decimal_to_binary
import hide_creditcard
import calculator
import x_equal_to_o
import discount
import repeat_character

list_of_numbers = [4, 3, 2, 9, 1]
sort_a_list.solve(list_of_numbers, 0)
print(list_of_numbers)

RADIAN = 5 * math.pi
print(radian_to_degree.solve(RADIAN))

TEXT = "This iS a StrIng"
print(count_vowels.solve(TEXT))

NUM = 1204
print(decimal_to_binary.solve(NUM))

credit_card = "123456790"
print(hide_creditcard.solve(credit_card))

fnum = 3
snum = 4
op = '/'
print(calculator.solve(fnum, op, snum))

text = "xoxo"
print(x_equal_to_o.solve(text))

price = 50
discount_percentage = 20
print(discount.solve(price, discount_percentage))

repeat_text = 'Hello'
print(repeat_character.solve(repeat_text))