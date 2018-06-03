def cube(x): return x**3

def add(x,y):return x+y

if __name__ == "__main__":
    import sys
    print map(cube, range(1, int(sys.argv[1])))
    print map(add, range(1, int(sys.argv[1])), range(1, int(sys.argv[1])))
