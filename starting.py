def f(a, *args, **kwargs):
    print ("a", a)
    print ("args", args)
    print ("kwargs", kwargs)

f(1,2,3,"frent",4,5)
