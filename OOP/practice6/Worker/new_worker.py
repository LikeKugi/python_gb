from .worker import Worker


def create_worker(name: str = '', last_name: str = '', salary: int = 0, passport_id: int = 0,
                  phone_number: int = 0, cabinet: int = 0):
    new_worker = Worker(name=name, last_name=last_name, salary=salary, passport_id=passport_id,
                        phone_number=phone_number, cabinet=cabinet)

    return new_worker
