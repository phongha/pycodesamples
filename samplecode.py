# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time, sys
import datetime
from dateutil import tz
import regex as re

def utcnow() :
    return datetime.datetime.now(tz=tz.tzutc()).isoformat()

def isPhoneNumber(text) :
    phoneNumber = re.compile(r'(\(?)\d{3}(\)?)-\d{3}-\d{4}')
    
    if(phoneNumber.search(text)!=None):
        return True
    else: return False

def spam():
    eggs = 'local eggs'
    #global eggs
    #eggs = 'global eggs'
    return eggs 

def main():
    #print ("Hello Universe.")
    #print (sys.path)
    #for pth in sys.path : print (pth, end='\n')
    #for hpth in sys.path_hooks : print (hpth, end='\n')
    #print ("UTC now: ", utcnow())
    #utcnow()
    #for tzs in tz. : print (tzs, end='\n')
    
    #RegEx
    # text = "(470)-861-8608"
    # print ("is this a phone number %s? ", text, isPhoneNumber(text))
    
    # total = 0
    # for i in range (1, 101, 2 ):
    #     total += i
    # print ("The total is ", total )
    
    # eggs = "global eggs"
    # print(spam(), eggs, sep=',')
           
    # indent = 0
    # indentIncreasing = True    
    # try:
    #     while True:
    #         print(' ' * indent, end='')
    #         print('************ indent = %s' % (indent))
    #         #print("indent = %s" % (indent), end='')
    #         time.sleep(0.1)
    #         if indentIncreasing == True:
    #             indent += 1
    #             if indent == 20:
    #                 indentIncreasing = False
    #         else:
    #             indent -= 1
    #             if indent == 0:
    #                 indentIncreasing = True   
    # except KeyboardInterrupt:
    #     sys.exit(0)
        
    #Lists are mutable. Mutable means references are assigned not values copied,
    #during assignments. Parameters are passed by reference!!!
    mylist = ['0', '1', '2', '3']
    print( mylist[0:len(mylist)])
    myLongList = mylist * 3
    print(myLongList)
    del mylist[1]
    print (mylist)

    #mutable & immutable
    #lists are mutable while Tuples are not
    
    try:
        
        myList = ['0', '1', '2', '3']
        #the following is illegal with immutable objects like Tuple & string
        myList.insert(myList.index('0'), 'zero')
        myList.insert(myList.index('1'), 'one')
        myList.insert(myList.index('2'), 'two')
        myList.insert(myList.index('3'), 'three')
        print ("Before %s" % (myList))
        
        myTuple = tuple(myList)
        #this will cause a type exception
        myTuple.remove('zero')
        print ('After: %s' % (myTuple))
        
    except TypeError:
        print("TypeError: trying to modify mutable value like Tuples")
        sys.exit(-1)
    except AttributeError as e:
        print("AttributeError: this happens when calling a method that is not \
              implemented for a class of object, e" % (e))
        print("%s" % (e))
    except Exception as e :
        print ("Exception: %s" % (e))
        sys.exit(-1)
    

    
if __name__ == '__main__':
    main()
