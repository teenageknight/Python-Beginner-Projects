import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

def logger(func):
    def log_func(*arg):
        logging.info('Running the function "{}" with the greatest of ease.'.format(func.__name__))
    return log_func

def add(x,y):
    return x+y

add_logger = logger(add)

add_logger(3,3)
