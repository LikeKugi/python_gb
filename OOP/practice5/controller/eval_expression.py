from .confirm_expression import confirm_expression

def eval_expression(expression: str) -> tuple[str, int]:
    if confirm_expression(expression):
        answer = eval(expression)
        return f'{expression}={answer}',answer