from functions.write_file import write_file
from functions.run_python_file import run_python_file


def test():
    result = run_python_file("calculator", "main.py")
    print(f"Test 1: {result}")

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(f"Test 2: {result}")

    result = run_python_file("calculator", "tests.py")
    print(f"Test 3: {result}")

    result = run_python_file("calculator", "../main.py")
    print(f"Test 4: {result}")

    result = run_python_file("calculator", "nonexistent.py")
    print(f"Test 5: {result}")


if __name__ == "__main__":
    test()
