from .eval_expression import eval_expression
from model import Expressions


def init_calc() -> Expressions:
    history = Expressions()
    return history


def add_calc(*, history: Expressions, value: str) -> dict[int, dict[str, str]]:
    result = eval_expression(value)
    history.append(result)
    return history.history
