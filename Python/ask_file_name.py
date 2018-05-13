def ask_file_name():
    while True:
        filename = input("Type a file name: ")
        try: 
            open(filename, "r")
            return filename
        except:
            continue
