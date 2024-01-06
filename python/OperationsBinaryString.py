operators_dict = {'A': '&', 'B': '|', 'C': '^'}
bin_str = "1C0C1C1A0B1"
char_list = list(bin_str)

def OperationsBinaryString(char_list):
    i = 1
    while len(char_list) > 1:
        if char_list[i] in operators_dict:
            operator = operators_dict[char_list[i]]
            x = int(char_list[i - 1]) & int(char_list[i + 1]) if operator == '&' else \
                int(char_list[i - 1]) | int(char_list[i + 1]) if operator == '|' else \
                int(char_list[i - 1]) ^ int(char_list[i + 1]) if operator == '^' else None

            print(f"{char_list[i - 1]} {operator} {char_list[i + 1]} : {x}")
            char_list.pop(i - 1)
            char_list.pop(i - 1)
            char_list.pop(i - 1)
            char_list.insert(i - 1, str(x))

        print(char_list)

OperationsBinaryString(char_list)
