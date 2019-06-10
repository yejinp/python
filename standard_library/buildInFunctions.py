#/bin/python


def main():
    print "abs()", abs(-9), abs(89)
    print "all()",all([[],99]), all([1,23])
    print "any()",any([[],99]), any([1,23])
    print "basestring()",isinstance('123',basestring)
    print "bin()", bin(99)
    print "bool()", bool([]),bool(0), bool(6)
    print "bytearray()", bytearray("1ii234"), bytearray()
    print "callable()", callable(basestring), callable(5)
    print "chr()", chr(90)
    print "classmethod() Not implement!"
    print "cmp()", cmp(6,8), cmp(9,8), cmp([],[[]])
    print "compile() Not implement"
    print "complex()", complex(6,8), complex(0,6), complex(8,0)
    print "delattr() Not implement"
    print "dict()", dict(),dict(a='1', b='6',c=[]), dict([('1',1), ('2',2)])
    c,d,a = '567', 6,8
    print "dir()",dir()
    print "divmod()", divmod(9,5),divmod(95.9,0.8)
    print "enumerate()", list(enumerate(['Spring', 'Summer', 'Fall', 'Winter']))
    print 'eval()',eval('d+5')
    print 'execfile() Not implement' #, execfile('/bin/date')
    print 'filter() Not implement' #, filter()
    print 'float()',float(88.88), float('99.9999999')
    print 'format()', format('5')
    print 'frozenset()',frozenset([1,2,3])
    print 'getattr() Not implement'
    print 'globals()', globals()
    print 'hasattr()', hasattr(d,'a')
    print 'hash()', hash(c)
    #print 'help()',help()
    print 'hex(56)',hex(56)
    print 'id(a)', id(a)
    #print 'input()',input()
    print 'int(9), int(\'99\',16)', int(9),int('99',16)
    print 'isinstance(5,int)',isinstance(5,int)
    print 'issubclass() Not Implement'#,issubclass()
    print 'iter() Not implement'
    print 'len()', len([[],[]]), len('abcd')
    print 'list()',list(),list('abcd')
    print 'locals()', locals()
    print 'long()', long(),long('abcd',16)
    print 'map() Not implement'
    print 'max()',max(5,6,7,8,9,0),max([1,2,3,5,6,7,8])
    print 'memoryview() Not implement' #, memoryview(d)
    print 'min()',min(5,6,7,8,9,0),min([1,2,3,5,6,7,8])
    print 'next() Not implement'

if __name__ == "__main__":
    main()
