from src.yafr import FredClient

fred = FredClient()

print(fred.get_series(series_id="GNPCA"))
