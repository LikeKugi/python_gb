class Contact:
    """
    contact
    """
    _name: str | None
    _phone_number: list[int] | None

    def __init__(self, name: str | None = None, phone: str | None = None) -> None:
        if name:
            self.name = name
        else:
            self.name = phone
        if phone:
            self.phone_number = phone

    # -------------------------------------------------------------------------------
    # _phone_number
    # -------------------------------------------------------------------------------
    @property
    def phone_number(self) -> str:
        """
        get phone number
        :return: str
            phone number if number exists or empty string
        """
        if not self._phone_number:
            return ''
        if len(self._phone_number) < 5:
            return ''.join(str(self._phone_number))
        elif len(self._phone_number) < 8:
            return f'{self._phone_number[:-4]}-{self._phone_number[-4:-2]}-{self._phone_number[-2:]}'
        else:
            return f'{self._phone_number[0]}-{self._phone_number[1:-4]}-{self._phone_number[-4:-2]}-{self._phone_number[-2:]}'

    @phone_number.setter
    def phone_number(self, phone: str) -> None:
        for char in ['+', '(', ')', '-', '_']:
            phone = phone.replace(char, '')
        if phone.isdigit() and len(phone) < 12:
            self._phone_number = [int(el) for el in phone]
        else:
            self._phone_number = None

    # -------------------------------------------------------------------------------
    # _name
    # -------------------------------------------------------------------------------
    @property
    def name(self) -> str:
        """
        get name of contact
        :return: str
            name
        """
        return self._name.title()

    @name.setter
    def name(self, value: str) -> None:
        self._name = value.lower()

    # -------------------------------------------------------------------------------
    # __str__
    # -------------------------------------------------------------------------------
    def __str__(self) -> str:
        return f'''
        {self._name}
        \t{self._phone_number}\n
        '''
