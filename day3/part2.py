from string import ascii_lowercase, ascii_uppercase

lower_values = {letter: ascii_lowercase.index(letter)+1 for letter in ascii_lowercase}
upper_values = {letter: ascii_uppercase.index(letter)+27 for letter in ascii_uppercase}
LETTER_VALUES = lower_values|upper_values

def list_generator(input_file) -> list:
    with open(input_file, "r", encoding="utf-8") as file:
        raw_list = [line.rstrip() for line in file]
        return raw_list

def form_priorities(raw_list) -> list:
    int_list = [list(map(lambda char:LETTER_VALUES.get(char), group)) for group in raw_list]
    return int_list

def recurruing_finder(int_list) -> list:
    reccur_list = []
    for item in int_list:
        if not int_list.index(item)%3 == 0:
            continue
        for number in item:
            if number in item and number in int_list[int_list.index(item)+1] and number in int_list[int_list.index(item)+2]:
                reccur_list.append(number)
                break
    return(reccur_list)

def sum_values(list_with_values) -> int:
    return sum(list_with_values)


def main():
    list1 = list_generator("3_input.txt")
    int_list = form_priorities(list1)
    reccur_list = recurruing_finder(int_list)
    value = sum_values(reccur_list)
    print(value)


if __name__ == '__main__':
    main()
