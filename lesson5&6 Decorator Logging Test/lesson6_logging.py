import logging

logging.basicConfig(level=logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('log.txt')
file_handler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(file_handler)


def log(message):
    def log_decorator(func):
        def wrapper(*args, **kwargs):
            logger.debug(message)
            func(*args, **kwargs)

        return wrapper

    return log_decorator


@log('message to log')
def my_func():
    print('ABC')

my_func()
