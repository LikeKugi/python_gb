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
    calc = SelfDescriptor()
    quiz = SelfDescriptor()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.calc = False
        self.quiz = False

    def do_calc(self):
        self.stop_state()
        self.calc = True

    def do_quiz(self):
        self.stop_state()
        self.quiz = True

    def stop_state(self):
        self.quiz = False
        self.calc = False
