def get_greeting(name: str) -> str:
    return name


if __name__ == "__main__":
    message = get_greeting("World")
    print('Hello, ' + message + '!')
