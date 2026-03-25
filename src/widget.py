from masks import get_mask_account, get_mask_card_number


def mask_account_card(name_card):
    num = "1234567890"
    i_test = 0
    for i in name_card:
        if i in num:
            print(
                f"{name_card[0:i_test-1]} {name_card[i_test:i_test+4]} {name_card[i_test+4:i_test+6]}** **** {name_card[-4:]}"
            )
            break
        i_test += 1


# 1234567890123456
input_card_number = input("Введите номер карты: ")

# 12345678901234567890
input_mask_account = input("Введите номер счета: ")

get_mask_card_number(input_card_number)
get_mask_account(input_mask_account)

# Visa Platinum 7000792289606361
# Maestro 7000792289606361
# Maestro 1596837868705199
# Счет 64686473678894779589
# MasterCard 7158300734726758
# Счет 35383033474447895560
# Visa Classic 6831982476737658
# Visa Platinum 8990922113665229
# Visa Gold 5999414228426353
# MasterCard 7158300734726758
# Счет 73654108430135874305
name_card_input = input("Введите название и номер карты: ")
mask_account_card(name_card_input)
