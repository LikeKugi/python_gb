def confirm_expression(exp: str) -> bool:
    res = exp
    for char in ('/', '*', '-', '+', '.'):
        res = res.replace(char, '')
    return res.isdigit()