import time
def time_function(func, x,trials=10):
    """Records the time it takes a function to operate. """
    start=None
    end=None
    output:float
    output=50
    for i in range(trials):
        start=time.time()
        func(x)
        end=time.time()
        times=(end-start)
        print(times)
        if times<output:
            output=times
    
    return output

    
def time_function_flexible(f,args, trials=10):
    """ Allows for an arbritrary amount of arguments to test the necessary function"""
    output=0
    for arg in args:
        output+=arg
    
        
    return float(f(*args))



if __name__ == '__main__':
    # Some tests to see if time_function works
    def test_func(L):
        for item in L:
            item *= 2

    L1 = [i for i in range(10**5)]
    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10**6)] # should be 10x slower to operate on every item
    t2 = time_function(test_func, L2)

    print("t(L1) = {:.3g} ms".format(t1*1000))
    print("t(L2) = {:.3g} ms".format(t2*1000))
    print(time.time())