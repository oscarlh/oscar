#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#age = 6
#if age >= 18:
    #print('your age is', age)
    #print('adult')
#elif age >= 6:
    #print('your age is', age)
    #print('oscar')
#else:
    #print('your age is', age)
    #print('teenager')
#x = 0
#if x:
	#print('True')
#birth = input('birth: ')
#birth = int(birth)
#if birth < 2000:
	#print('00前')
#else:
	#print('00后')
#names = ['oscar','lh','yuanfang']
#for name in names:
	#print(name)
#sum = 0
#for x in [1,2,3,4,5,6,7,8,9,10]:
	#sum += x
#print(sum)

#def my_abs(x):
    #if x >= 0:
        #return x
    #else:
        #return -x
#print(my_abs(-9))

#import math

#def oscar(x, y, step, angle=0):
    #nx = x + step * math.cos(angle)
    #ny = y - step * math.sin(angle)
    #return nx, ny
#def oscar2(x):
    #return x * x
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
    print('end')

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)