#!/usr/bin/env python

def showMaxFactor(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            print 'largest factor of %d is %d' %\
                (num, count)
            break
        count -= 1
    else:
        print num, 'is prime'

def main():
    for eachNum in range(10, 21):
        showMaxFactor(eachNum)

if __name__ == "__main__":
    main()
