def main():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
        'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 
        'v', 'w', 'x', 'y', 'z'
    ]
    
    combinations_2 = get_combinations(letters, 2)
    combinations_3 = get_combinations(letters, 3)
    combinations_4 = get_combinations(letters, 4)
    
    save_to_file("combinations_2.txt", combinations_2)
    save_to_file("combinations_3.txt", combinations_3)
    save_to_file("combinations_4.txt", combinations_4)
    
    print(f"2'li kombinasyon sayısı: {len(combinations_2)}")
    print(f"3'lü kombinasyon sayısı: {len(combinations_3)}")
    print(f"4'lü kombinasyon sayısı: {len(combinations_4)}")

def get_combinations(lst, combination_length):
    combinations = []
    count = 2 ** len(lst)
    for i in range(1, count):
        binary_str = bin(i)[2:].zfill(len(lst))
        combination = ""
        for j in range(len(binary_str)):
            if binary_str[j] == '1':
                combination += lst[j]
        
        if len(combination) == combination_length:
            combinations.append(combination)
    return sorted(combinations)

def save_to_file(filename, combinations):
    with open(filename, "w") as file:
        for combo in combinations:
            file.write(combo + "\n")

if __name__ == "__main__":
    main()

#TODO: need to improve -> aba, abaa, abca.. 

"""
2'li kombinasyon sayısı: 300
3'lü kombinasyon sayısı: 2.300
4'lü kombinasyon sayısı: 12.650
"""
