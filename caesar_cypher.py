class Caesar:
    """
    Шифр Цезаря
    каждый символ в открытом тексте заменяется символом, находящимся на некотором постоянном числе позиций левее или правее него в алфавите
    """

    __alphabet: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z']  # 26
    __ENCODE: str = "encode"
    __DECODE: str = "decode"

    def __init__(self, shift: int):
        """
        Конструктор
        :param shift: сдвиг текста для алгоритма шифра
        """
        self._shift = shift

    def __caesar(self, text: str, direction: str) -> str:
        """
        Реализация алгоритма шифра Цезаря
        :param text: текст для шифрования|расшифрования
        :param direction: режим работы шифра (Encode, Decode)
        :return: зашифрованный|расшифрованный текст
        """
        converted_text = ""
        alphabet_len = len(self.__alphabet)
        dir_sign = 1 if direction == self.__ENCODE else -1
        for char in text:
            converted_char = char
            if char in self.__alphabet:
                index = (self.__alphabet.index(char) + (dir_sign * self._shift)) % alphabet_len
                converted_char = self.__alphabet[index]
            converted_text += converted_char
        return converted_text

    def encode(self, text: str) -> str:
        """
        Зашифровать текст
        :param text: текст для шифрования
        :return: зашифрованный текст
        """
        return self.__caesar(text, self.__ENCODE)

    def decode(self, text: str) -> str:
        """
        Расшифровать текст
        :param text: текст для расшифрования
        :return: расшифрованный текст
        """
        return self.__caesar(text, self.__DECODE)