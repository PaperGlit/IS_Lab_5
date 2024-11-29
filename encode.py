from feistel import Feistel
from validate import validate
from upload import upload


def encode():
    prompt_1 = input("Enter the string to encode: ")
    try:
        cipher_key, n = validate()
    except ValueError as e:
        raise e
    feistel = Feistel(cipher_key=cipher_key, n=n)
    encrypted = feistel.encrypt(prompt_1)
    print(f"Encrypted string: {encrypted}")
    prompt_2 = input("Do you want to save this string? (Y/N): ")
    if prompt_2.lower() == "y":
        try:
            upload(encrypted)
        except IOError as e:
            print(e)
