'''
Created on 2020. 8. 7.
@author: GDJ24
exam3.py : 간단한 계산기 함수
'''

def calc(var1,var2,oper):
    result = 0
    if oper == '+' :
        result = var1 + var2
    elif oper == '-' :
        result = var1 - var2
    elif oper == '*' :
        result = var1 * var2
    elif oper == '/' :
        result = var1 / var2
    return result

oper = input("choose an operator: +,-,*,/ =>")
var1 = int(input("enter first number=>"))
var2 = int(input("enter second number=>"))
res = calc(var1,var2,oper)
print("%d %s %d = %d" % (var1,oper,var2,res))
