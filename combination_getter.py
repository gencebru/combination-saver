def main():
    get_combination([ 1, 2, 3, 4])

def get_combination(lst):
    count = 2 ** len(lst)
    for i in range(1, count):
        binary_str = bin(i)[2:].zfill(len(lst))
        for j in range(len(binary_str)):
            if binary_str[j] == '1':
                print(lst[j], end='')
        print()

if __name__ == "__main__":
    main()
