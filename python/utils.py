def calculate_percentage(part, whole):
    if whole == 0:
        return 0.0
    return round((part / whole) * 100, 2)


def round_value(value, decimals=2):
    try:
        return round(float(value), decimals)
    except (TypeError, ValueError):
        return value


def to_records(df):
    return df.to_dict(orient="records")