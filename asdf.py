
def isInts(f):
    def asd(a,b):
        assert type(a) == int, "a not int"
        assert type(b) == int, "b not int"
        f(a,b)
    return asd


def request_types(*types):
    """
    When decorating function, give types that arguments should be
        @aretype(type1,type2,type3)
        def function(param1,param2,param3):
            pass
    """

    def return_test(f):
        """Runnable that is returned by decorator"""
        def test(*args):
            """Decorated functions parameters are passed to this function"""
            # check if every parameter is respective type

            for i in range(0,len(args)):
                assert len(args) == len(types), "Number of types given to decorator differ from number of arguments"
                assert type(args[i]) == types[i], "Wrong argument type. You gave '{}' of type {} when you needed {}"\
                    .format(args[i], type(args[i]), types[i])
            f(*args)
        return test
    return return_test


@request_types(int, int)
def moi(a,b)
    print("{}+{}={}".format(a,b,a+b))

a, b =1, 2
moi(a, b)

request_types(int, int)(moi)(a, b)

def asdf(a,b):
    assert type(a) == int, "not int"
    assert type(b) == int, "not int"