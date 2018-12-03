#!/bin/env python

class MyDataWithMethod(object):
    def printFoo(self):
        print 'You invoked printFoo()'

if __name__=="__main__":
    my_class=MyDataWithMethod()
    my_class.printFoo()
