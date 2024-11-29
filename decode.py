from feistel import Feistel
from validate import validate


def decode():
    prompt_1 = input("Enter the amount of blocks: ")
    try:
        blocks = int(prompt_1)
    except ValueError:
        raise ValueError("The value must be a non-negative integer")
    if blocks < 1: raise ValueError("The value must be a non-negative integer")
    encoded = []
    for i in range(blocks):
        prompt_2 = input(f"Enter the encoded string to decode (Block {i+1}): ")
        try:
            encoded.append(int(prompt_2))
        except ValueError:
            print("The value must be an integer")
    try:
        cipher_key, n = validate()
    except ValueError as e:
        raise e
    feistel = Feistel(cipher_key=cipher_key, n=n)
    decrypted = feistel.decrypt(encoded)
    print(f"Decrypted string: {decrypted}")
