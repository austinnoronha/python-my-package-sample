# src/sample_package/sample_package.py
from lib.helpers import generate_uuid


def hello_world():
    """Return a greeting message."""
    uuid_str = generate_uuid()
    return f"Hello, World, your request no is: {uuid_str}"

if __name__ == '__main__':
    msg = hello_world()
    print(f'Message: {msg}')