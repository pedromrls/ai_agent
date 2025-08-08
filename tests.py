from functions.write_file import write_file


def test():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f'Test 1: {result}')

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f'Test 2: {result}')

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f'Test 3: {result}')

if __name__ == "__main__":
    test()


