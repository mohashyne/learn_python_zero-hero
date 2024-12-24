if len(sys.argv) == 1:
    print("USAGE: python app.py <password>")
else:
    password = sys.argv[1]
    print(f"Password: {password}")