class SelfDescriptor:
    __slots__ = ['name']

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value:
            instance.__dict__[self.name] = True
        else:
            instance.__dict__[self.name] = False


class BotState:
    """
    finite state for bot

    bool values
    """
    _instance = None
    ask = SelfDescriptor()
    asked = SelfDescriptor()
    answers = SelfDescriptor()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.ask = False
        self.asked = False
        self.answers = False

    def do_ask(self):
        self.stop_state()
        self.ask = True

    def do_asked(self):
        self.stop_state()
        self.asked = True

    def do_answers(self):
        self.stop_state()
        self.answers = True

    def stop_state(self):
        self.ask = False
        self.asked = False
        self.answers = False
