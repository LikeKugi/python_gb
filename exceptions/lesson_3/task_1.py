# Создать статический метод который принимает на вход три параметра: login, password и confirmPassword.
# Login должен содержать только латинские буквы, цифры и знак подчеркивания.
# Длина login должна быть меньше 20 символов. Если login не соответствует этим требованиям,
# необходимо выбросить WrongLoginException.
# Password должен содержать только латинские буквы, цифры и знак подчеркивания.
# Длина password должна быть меньше 20 символов. Также password и confirmPassword должны быть равны.
# Если password не соответствует этим требованиям, необходимо выбросить WrongPasswordException.
# WrongPasswordException и WrongLoginException - пользовательские классы исключения с двумя конструкторами –
# один по умолчанию, второй принимает сообщение исключения и передает его в конструктор класса Exception.
# Обработка исключений проводится внутри метода.
# Используем multi-catch block.
# Метод возвращает true, если значения верны или false в другом случае.
import re


class WrongPasswordException(Exception):
    pass


class WrongLoginException(Exception):
    pass


def get_str(*args):
    return input(*args)


def confirm_name(name):
    pattern = re.compile(r'^[a-z0-9_]+\b', re.I)
    return (0 < len(name) < 20) and not len(re.sub(pattern, '', name))


def confirm_data(name, pwd, cfrm_pwd):
    if not confirm_name(name):
        raise WrongLoginException(f'{name} must be length less than 20 and contains only a-z 0-9 _')
    if pwd != cfrm_pwd or not confirm_name(pwd):
        raise WrongPasswordException(f'password must be length less than 20 and contains only a-z 0-9 _')
    return True


def main():
    login = get_str('input login: ')
    password = get_str('input password: ')
    confirm_password = get_str('confirm password: ')
    try:
        result = confirm_data(login, password, confirm_password)
        if result:
            print('ok')
        return True
    except WrongLoginException as e:
        print(e)
        return False
    except WrongPasswordException as e:
        print(e)
        return False


def test_regular():
    pattern = re.compile(r'[A-Za-z0-9]*_[A-Za-z0-9]*')
    print(re.match(pattern, 'Eq0_wqй'))


if __name__ == '__main__':
    main()
