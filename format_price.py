import argparse
import re


def format_price(price):
    price_str = str(price).strip()
    clear_str = re.sub(r"[., ]", "", price_str)
    if not clear_str.isdigit():
        return None

    digit_str = price_str.split('.')
    numbers_str = decimal_str = ""

    if len(digit_str) > 0:
        numbers_str = re.sub(
            r"[, ]",
            "",
            digit_str[0]
        )

    if len(digit_str) > 1:
        decimal_str = re.sub(
            r"[, ]",
            "",
            digit_str[1]
        )

    reverse_price = numbers_str[::-1]
    space_price = ' '.join(
        [
            reverse_price[key_index:key_index+3] for key_index in range(
                    0, len(reverse_price), 3
                )
        ])
    decimal_str = decimal_str.rstrip("0")

    return "{}{}".format(
                space_price[::-1],
                '.'+decimal_str if len(decimal_str) > 0 else ""
            )

if __name__ == '__main__':
    aparser = argparse.ArgumentParser()
    aparser.add_argument(
        'price_input',
        type=float,
        help="Price input string to format"
    )
    args = aparser.parse_args()
    price = format_price(args.price_input)
    if price:
        print(price)
    else:
        print("Введено недопустимое число")
