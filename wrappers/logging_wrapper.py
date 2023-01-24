import logging

# Configure logging
logging.basicConfig(level=logging.INFO)


def logging(func):
    def wrap(*args, **kwargs):
        logging.info(args)
        return wrap

    return logging


if __name__ == '__main__':
    ...
