from caesar_cypher import Caesar


def test_caesar_failed():
    """
    Не валидная проверка на корректную зашифровку и последующую расшифровку текста со сдвигом 15
    """
    decrypted_text = "ilumination"
    encrypted_text = "vyhzvangvba"  # текст со сдвигом 13
    caesar = Caesar(15)
    check_encrypted_text = caesar.encode(decrypted_text)
    check_decrypted_text = caesar.decode(check_encrypted_text)
    assert check_encrypted_text == encrypted_text, f"Ошибка: зашифрованный текст: '{check_encrypted_text}' != '{encrypted_text}'"
    assert check_decrypted_text == decrypted_text, f"Ошибка: расшифрованный текст: '{check_decrypted_text}' != '{decrypted_text}'"
