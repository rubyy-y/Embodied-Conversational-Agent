# import numpy as np
# import pandas as pd
# import plotly.express as px

# from datetime import date, timedelta
# np.random.seed(42)

# # 1. how much playtime in last month per day/week

# # get n days ago for start of dataframe
# start_date = (date.today() - timedelta(days=31)).strftime(f"%Y/%m/%d")

# # dataframe: 1 column and 31 rows (days) of random floats
# df = pd.DataFrame(np.random.uniform(low=30.0, high=240.0, size=31))

# # with probability of 20% not played at all
# for i, day in enumerate(df[0]):
#     if np.random.randint(10) <= 2:
#         df[0][i] = 0

# # index from 31 days ago and rename column
# df.index = pd.date_range(start_date, periods=df.shape[0])
# df.columns = ['minutes_played'] 

# fig = px.bar(df, x=df.index, y='minutes_played')
# # fig.show()

# # fig.write_image("/static/images/plot1.png")