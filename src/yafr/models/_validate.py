from yafr.models.models import Series


def validate_series(series: dict) -> Series:
    series["fred_id"] = series["id"]
    del series["id"]
    return Series(**series)
