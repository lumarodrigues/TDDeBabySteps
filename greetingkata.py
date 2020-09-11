def greet(name=""):
    if isinstance(name, list):
        name.insert(-1, 'and')
        name = ', '.join(name).replace(', and,', ' and')
        return f"Hello, {name}!"

    if name.strip():
        if name.isupper():
            return f"HELLO, {name}!"
        else:
            return f"Hello, {name}!"
    else:
        return "Hello, my friend!"
