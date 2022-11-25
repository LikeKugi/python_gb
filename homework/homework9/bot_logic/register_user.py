import pickle
import os


def _open_users() -> dict:
    if os.path.isfile('user.bin'):
        with open('user.bin', 'rb') as inf:
            users = pickle.load(inf)
            return users
    else:
        return {}


def _save_users(users: dict) -> None:
    with open('user.bin', 'wb') as ouf:
        pickle.dump(users, ouf)


def _is_user(users: dict, user_id: int) -> bool:
    if user_id in users:
        return True
    return False


def _add_user(users: dict, user_id: int, username: tuple) -> dict:
    users[user_id] = username
    return users


def main_register(message) -> str:
    user_id = message.from_user.id
    username = (message.from_user.first_name, message.from_user.last_name)
    users = _open_users()
    if _is_user(users, user_id):
        return f'User in users'
    else:
        users = _add_user(users, user_id, username)
        _save_users(users)
        return f'User added'


def get_users_ids() -> list:
    users = _open_users()
    return list(users.keys())


if __name__ == '__main__':
    users = _open_users()
    print(users)
