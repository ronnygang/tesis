def decorator_lowercase(function):   # defining python decorator
    def wrapper():
        func = function()
        input_lowercase = func.lower()
        return input_lowercase
    return wrapper


@decorator_lowercase    ##calling decoractor
def intro():                        #Normal function
    return 'Hello,I AM SAM'

print(intro())