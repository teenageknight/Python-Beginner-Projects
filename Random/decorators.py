# Deccorators


def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print('display function ran')

display()
