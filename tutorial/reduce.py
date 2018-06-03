#!/usr/bin/python

def add(x,y): return x+y

if __name__ == "__main__":
    import sys
    print reduce(add, range(1, int(sys.argv[1])))
