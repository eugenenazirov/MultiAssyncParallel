class Event:
    def __init__(self):
        self.__handlers = []

    def __call__(self, *args, **kwargs):
        for f in self.__handlers:
            f(*args, **kwargs)

