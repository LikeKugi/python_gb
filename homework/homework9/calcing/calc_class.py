class Calculator:
    class CalculatorException(Exception):
        pass

    _expression: str

    def __init__(self, expression: str):
        self.expression = expression

    @property
    def expression(self):
        return self._expression

    @expression.setter
    def expression(self, value: str):

        val_expression = value
        for el in {'/', '*', '-', '+', '.', ' ', '(', ')'}:
            val_expression = val_expression.replace(el, '')

        if val_expression.isdigit():
            value = value.replace(' ', '')
            for el in {'/', '*', '-', '+', '.'}:
                value = value.replace(el, f' {el} ')
            self._expression = value
        else:
            raise self.CalculatorException(f'Not an expression: {value!r} should contains only digits and "/*-+."')

    def __str__(self):
        return f'{self._expression} = {eval(str(self._expression))}'

    def __repr__(self):
        return f'Calculator({self.expression!r})'


if __name__ == '__main__':
    a = Calculator('1   +( 2-3   )*4')
    print(a)