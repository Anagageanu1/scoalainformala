import pandas as pd
import matplotlib.pyplot as pl

#print(pd,__version__)
a = {'x': 1, "y":7, "z": 2}
variabila = pd.Series(a, index = a.keys())
variabila = pd.Series(a, index = ['x', 'y'])

print(variabila)
data =  {'key1:' [0,1,2],
         'key2:' [3,4,5]
}
variabila = pd.DataFrame(data, index = ['linie1', 'linie2', 'linie3'])
print(variabila['key2'])

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

# df1 = None
# for x in df.index:
#   print(df.loc[x, 'AL'])
#   if df.loc[x, 'AL'] == ':':
#     df1 = df.drop(x)
#
# df.plot(kind='scatter',x='AT', y='BE')
# df['AT'].plot(kind='hist')
# plt.show()
# print(df.head(2))
# print(df.tail(3))

# new_df = df.dropna(inplace=True)
# print(new_df)
# print(df.fillna(0))

# df['AL'].fillna(0, inplace=True)
# print(df)

# df.loc[7,'AL'] = 45
# print(df)

