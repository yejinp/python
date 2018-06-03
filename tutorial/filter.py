#filter tester

def f(x): return x % 3 == 0 or x % 5 ==0

if __name__ == "__main__":
    import sys
    print filter(f, range(0, int(sys.argv[1])))
