class Calculator:
    class CalculatorException(Exception):
        pass

    _expression: str

    def __init__(self, expression: str) -> None:
        self.expression = expression

    @property
    def expression(self) -> str:
        return self._expression

    @expression.setter
    def expression(self, value: str) -> None:

        val_expression = value
        for el in {'/', '*', '-', '+', '.', ' ', '(', ')'}:
            val_expression = val_expression.replace(el, '')

        if val_expression.isdigit():
            value = value.replace(' ', '')
            self._expression = value
        else:
            raise self.CalculatorException(f'Not an expression: {value!r} should contains only digits and "/*-+."')

    def __str__(self) -> str:
        value = self._expression
        for el in {'/', '*', '-', '+', '.'}:
            value = value.replace(el, f' {el} ')
        value = value.replace('*  *', '**')
        return f'{value} = {eval(str(self._expression))}'

    def __repr__(self) -> str:
        return f'Calculator({self.expression!r})'


if __name__ == '__main__':
    a = Calculator('1   +( 2-3   )*4')
    print(a)
    b = Calculator('5*(2+4)**6')
    print(b)
