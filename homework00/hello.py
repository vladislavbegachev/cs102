def get_greeting(name: str) -> str:
    return "Hello, " + name + "!"


if __name__ == "__main__":
    Message = get_greeting("World")
    print(Message)
