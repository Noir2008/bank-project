def get_mask_card_number(card_number):
    print(f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:16]}")

def get_mask_account(mask_account):
    print(f"**{mask_account[-4:]}")

# 1234567890123456
input_card_number = input("Введите номер карты: ")

# 12345678901234567890
input_mask_account = input("Введите номер счета: ")

get_mask_card_number(input_card_number)
get_mask_account(input_mask_account)