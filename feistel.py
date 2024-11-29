import random


class Feistel:
    def __init__(self, cipher_key, n = 32, rounds = 20):
        self.key = cipher_key
        self.n = n
        self.rounds = rounds
        self.modulo = 2 ** n
        self.subkeys = self._generate_subkeys()

    def _generate_subkeys(self):
        random.seed(self.key)
        return [random.randint(1, self.modulo - 1) for _ in range(self.rounds)]

    def _feistel_function(self, half_block, subkey):
        return (half_block * subkey) % self.modulo

    def _feistel_round(self, left, right, subkey):
        new_left = right
        new_right = left ^ self._feistel_function(right, subkey)
        return new_left, new_right

    def _str_to_blocks(self, text):
        block_size = self.n // 8
        text_bytes = text.encode()
        padding_length = (-len(text_bytes)) % (block_size * 2)
        text_bytes += b'\x00' * padding_length
        return [int.from_bytes(text_bytes[i:i + block_size * 2], 'big')
                for i in range(0, len(text_bytes), block_size * 2)]

    def _blocks_to_str(self, blocks):
        block_size = self.n // 8
        text_bytes = b''.join(block.to_bytes(block_size * 2, 'big') for block in blocks)
        return text_bytes.rstrip(b'\x00').decode()

    def encrypt_block(self, text: int):
        left = (text >> self.n) & (self.modulo - 1)
        right = text & (self.modulo - 1)
        for i in range(self.rounds):
            left, right = self._feistel_round(left, right, self.subkeys[i])
        return (left << self.n) | right

    def decrypt_block(self, ciphertext: int):
        left = (ciphertext >> self.n) & (self.modulo - 1)
        right = ciphertext & (self.modulo - 1)
        for i in reversed(range(self.rounds)):
            right, left = self._feistel_round(right, left, self.subkeys[i])
        return (left << self.n) | right

    def encrypt(self, text: str):
        blocks = self._str_to_blocks(text)
        encrypted_blocks = [self.encrypt_block(block) for block in blocks]
        return encrypted_blocks

    def decrypt(self, encrypted_blocks):
        decrypted_blocks = [self.decrypt_block(block) for block in encrypted_blocks]
        return self._blocks_to_str(decrypted_blocks)
