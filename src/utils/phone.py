def prepare_phone_number(phone_number: str) -> str:
    if phone_number.startswith('+7') and len(phone_number) == 12:
        res = phone_number.replace('+7', '8')
    else:
        res = phone_number

    return res
