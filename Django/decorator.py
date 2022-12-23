def log(func):
    def wrapperFunc():
        print("*** %s() called" % func.__name__)
        return func()
    return wrapperFunc()

@log
def foo():
    print("inside foo()")