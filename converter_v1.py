import random
import numpy
import matplotlib
import sympy

# def check(f_some_str, f_res, f_index, f_signs, f_signs_left, f_signs_num, f_op_gaps_num):
#     print(f_res)
#     if f_index <= len(f_some_str) - 1:
#
#         index = 0 + f_index
#         signs_left = 0 + f_signs_left
#         signs = f_signs
#
#         if f_some_str[index].isupper():
#
#             if f_some_str[index] == 'A':
#                 aux = '+'
#
#             if f_some_str[index] == 'K':
#                 aux = '*'
#
#             if f_some_str[index] == 'C':
#                 aux = '-->'
#
#             if f_some_str[index] == 'E':
#                 aux = '<->'
#
#             if f_some_str[index] == 'N':
#                 f_res += '(~'
#             else:
#                 f_res += '('
#                 f_op_gaps_num += 1
#
#
#             if f_some_str[index + 1].isupper():
#                 signs.append(aux)
#                 check(f_some_str, f_res, index + 1, signs, signs_left, f_signs_num, f_op_gaps_num)
#             else:
#                 f_res += f_some_str[index + 1] + aux
#                 f_signs_num += 1
#                 signs_left += 1
#                 check(f_some_str, f_res, index + 2, f_signs, signs_left, f_signs_num, f_op_gaps_num)
#
#         else:
#             # if gaps == 0:
#             #     f_res += f_some_str[index] + helper_sign
#             #     print(f_res)
#             #
#             #     signs_left += 1
#             #     check(f_some_str, f_res, index + 1, '', signs_left)
#             # else:
#                 # f_res += f_some_str[index] + ')' + helper_sign
#
#             f_res += f_some_str[index]
#
#             if f_signs_num < f_op_gaps_num and f_signs_num < 5 :
#                 f_res += ')'
#                 signs_left -= 1
#             else:
#                 for _ in range(signs_left):
#                     f_res += ')'
#                     signs_left -= 1
#
#             if len(signs) != 0:
#                 f_res += signs.pop()
#                 f_signs_num += 1
#             signs_left += 1
#
#             check(f_some_str, f_res, index + 1, signs, signs_left, f_signs_num, f_op_gaps_num)
#
#
# us_input = input()
#
# check(us_input, '', 0, [], 0, 0, 0)
#
# # CKpAqra
# KpAqr
# CKpqArs
# ECKpqArsa
# CCpqCCqrCpr
# ACCpqCCqrCprd


# FROMULA CONVERTER -^-

formula = input()

opened = 0
closed = 0

for x in range(len(formula)):
    if formula[x] == '(' :
        opened += 1
    if formula[x] == ')' :
        closed += 1
    if opened == closed:
        part1 = formula[:x + 1]
        if formula[x + 1] != '<':
            part2 = formula[x + 2:]
        else: part2 = formula[x + 3:]
        break

print(part1, part2)

#(p>(~p))<>p