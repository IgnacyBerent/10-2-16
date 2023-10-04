bin_to_hex_dict = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
hex_to_bin_dict = {v: k for k, v in bin_to_hex_dict.items()}


def dec_to_bin(num):
    num = int(num)
    bin_num = []
    while num != 0:
        bin_num.append(str(num % 2))
        num = num // 2
    bin_num.reverse()

    return ''.join(bin_num)


def bin_to_hex(bin_num):
    bin_num = list(bin_num)
    while len(bin_num) % 4 != 0:
        bin_num.insert(0, '0')
    bin_sorted = []
    for i in range(0, len(bin_num), 4):
        new_element = ''
        for j in range(4):
            new_element += bin_num[i+j]
        bin_sorted.append(new_element)
    result = [bin_to_hex_dict[num] for num in bin_sorted]
    return ''.join(result)


def dec_to_hex(num):
    return bin_to_hex(dec_to_bin(num))


def hex_to_bin(num):
    num_list = list(num)
    bin_num = [hex_to_bin_dict[n] for n in num_list]
    bin_num = ''.join(bin_num)
    bin_num = list(bin_num)
    while bin_num[0] == 0:
        bin_num.pop(0)
    return ''.join(bin_num)

def bin_to_dec(num):
    dec_sum = 0
    for i, digit in enumerate(num):
        dec_sum += int(digit) * 2**i
    return dec_sum


def hex_to_dec(num):
    return bin_to_dec(hex_to_bin(num))
