def upload(data, cipher_key, n):
    file_name = input("Enter file name: ")
    if file_name.strip() != "":
        if not file_name.endswith(".txt"):
            file_name += ".txt"
        try:
            with open(file_name, 'w', encoding="utf-8") as f:
                for i in data:
                    f.write(str(i) + " ")
                f.write(f"\nKey: {cipher_key}\n"
                        f"n: {n}")
                print("The data was uploaded successfully")
        except IOError as e:
            print(f"Error uploading data: {e}")
    else:
        raise IOError("Please enter a valid file name")
