from encode import encode
from decode import decode


class Console:
    def __init__(self):
        self.main()

    @staticmethod
    def main():
        while True:
            prompt = input("1 - Encode the string\n"
                           "2 - Decode the string\n"
                           "Your choice: ")
            match prompt:
                case '1':
                    try:
                        encode()
                    except ValueError as e:
                        print(e)
                        continue
                case '2':
                    try:
                        decode()
                    except ValueError as e:
                        print(e)
                case _:
                    return
