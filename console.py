from feistel import Feistel
from upload import upload


class Console:
    def __init__(self):
        self.main()

    def main(self):
        while True:
            prompt = input("1 - Encode the string\n"
                           "2 - Decode the string\n"
                           "Your choice: ")
            match prompt:
                case '1':
                    try:
                        self.encode()
                    except ValueError as e:
                        print(e)
                        continue
                case '2':
                    try:
                        self.decode()
                    except ValueError as e:
                        print(e)
                case _:
                    return

    def decode(self):
        prompt_1 = input("Enter the amount of blocks: ")
        try:
            blocks = int(prompt_1)
        except ValueError:
            raise ValueError("The value must be a non-negative integer")
        if blocks < 1: raise ValueError("The value must be a non-negative integer")
        encoded = []
        for i in range(blocks):
            prompt_2 = input(f"Enter the encoded string to decode (Block {i + 1}): ")
            try:
                encoded.append(int(prompt_2))
            except ValueError:
                print("The value must be an integer")
        try:
            cipher_key, n = self.validate()
        except ValueError as e:
            raise e
        feistel = Feistel(cipher_key=cipher_key, n=n)
        decrypted = feistel.decrypt(encoded)
        print(f"Decrypted string: {decrypted}")

    def encode(self):
        prompt_1 = input("Enter the string to encode: ")
        try:
            cipher_key, n = self.validate()
        except ValueError as e:
            raise e
        feistel = Feistel(cipher_key=cipher_key, n=n)
        encrypted = feistel.encrypt(prompt_1)
        print(f"Encrypted string: {encrypted}")
        prompt_2 = input("Do you want to save this string? (Y/N): ")
        if prompt_2.lower() == "y":
            try:
                upload(encrypted, cipher_key, n)
            except IOError as e:
                print(e)

    @staticmethod
    def validate():
        c_k = input("Enter the key: ")
        n_val = input("Enter the value of N: ")
        try:
            cipher_key = int(c_k)
            n = int(n_val)
        except ValueError:
            raise ValueError("The key and the value of N must be integers")
        return cipher_key, n