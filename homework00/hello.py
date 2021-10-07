def get_greeting(name: str) -> str:
    message = "Hello, " + name + "!"
    return message

if __name__ == "__main__":
    message = get_greeting("World")
    print(message)
