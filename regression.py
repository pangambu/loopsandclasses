import pandas as pd
import quandl as qd
import matplotlib as plt
import numpy as np

qd.ApiConfig.api_key = ""


aapl_data = qd.get('EOD/AAPL')

Apple = aapl_data.head()
print(Apple)