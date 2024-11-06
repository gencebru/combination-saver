def main():
    combinations = get_combination([
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
        'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 
        'v', 'w', 'x', 'y', 'z'
    ])
    
    with open("combinations.txt", "w") as file:
        for combo in combinations:
            file.write(combo + "\n")
    

    print(f"Oluşturulan kombinasyon sayısı: {len(combinations)}")

def get_combination(lst):
    combinations = []
    count = 2 ** len(lst)
    for i in range(1, count):
        binary_str = bin(i)[2:].zfill(len(lst))
        combination = ""
        for j in range(len(binary_str)):
            if binary_str[j] == '1':
                combination += lst[j]
        combinations.append(combination)
    return sorted(combinations)

if __name__ == "__main__":
    main()

"""
Oluşturulan kombinasyon sayısı: 33.554.431
"""