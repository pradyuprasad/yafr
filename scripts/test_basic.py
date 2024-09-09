from src.yafr import FredClient

try:
    fred = FredClient()
    print("initialized successfully!")
except Exception as e:
    print("failed to initialize")
    print(e)
