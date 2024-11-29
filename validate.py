def validate():
    c_k = input("Enter the key: ")
    n_val = input("Enter the value of N: ")
    try:
        cipher_key = int(c_k)
        n = int(n_val)
    except ValueError:
        raise ValueError("The key and the value of N must be integers")
    return cipher_key, n
