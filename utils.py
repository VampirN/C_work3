def sorted_operations_status(data):
    '''Сортировка операций по статусу executed'''

    new_data = []
    for transaction in data:
        if transaction and transaction.get('state') == 'EXECUTED':
            new_data.append(transaction)

    return new_data


def sorted_operation_date(data):
    '''Сортировка операций по дате'''

    data = sorted(data, key=lambda x: x['date'], reverse=True)

    return data[:5]


def message_conversion(item):
    '''Правка формата вывода сообщения'''

    date = get_date(item.get('date'))
    desc = item.get("description")
    from_ = masked(item.get("from"))
    to_ = masked(item.get("to"))
    amount = item.get("operationAmount").get("amount")
    currency = item.get("operationAmount").get("currency").get("name")

    if from_:
        from_ += ' ->'
    else:
        from_ = ''

    return f"{date} {desc}\n{from_} {to_}\n{amount} {currency}"


def get_date(date):
    '''Формат времени'''

    date_raw = date[0:10].split(sep="-")

    return f"{date_raw[2]}.{date_raw[1]}.{date_raw[0]}"


def masked(number):
    '''Вывод маскировки в сообщение'''

    if number is None:
        return ""

    msg = number.split()

    if msg[0] == "Счет":
        number_hidden = mask_account(msg[-1])
    else:
        number_hidden = mask_card_number(msg[-1])

    return ' '.join(msg[:-1]) + ' ' + number_hidden


def mask_account(number: str):
    '''Маскировка номера счета'''

    if number.isdigit() and len(number) > 4:
        return f"**{number[-4:]}"
    else:
        raise ValueError("Номер счета некорректный")


def mask_card_number(number: str):
    '''Маскировка номера карты'''

    if number.isdigit() and len(number) == 16:
        return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
    else:
        raise ValueError("Номер карты некорректный")