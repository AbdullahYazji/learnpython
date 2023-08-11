convert_month = {
    "jan": "january",
    "feb": "february",
    "mar": "march"
}

print(convert_month["jan"])

print(convert_month.get("code"))

print(convert_month.get("code", "comment"))

# _________________________________________________________

convert_month = {
    0: 0,
    1: True,
    "mar": ["march", "march is the third month", 1, 2, 4]
}

print(convert_month.get("mar", "comment"))
