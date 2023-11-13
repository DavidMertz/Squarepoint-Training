```python
import pandas as pd

url = ("https://bitbucket.org/davidmertz/sample-data/raw/"
       "61872271984f66e3094c367cf90dfc4875a22e8d/NOAA-2019-partial.csv.gz")
t = pd.read_csv(url)
t['DATE'] = pd.to_datetime(temperatures.DATE, format="%Y-%m-%d")
t.set_index('DATE', inplace=True)
t = t.loc['2019-01-01', ['LATITUDE', 'LONGITUDE', 'MAX']]
t = t.loc[t.LATITUDE >= 45]
t['LATITUDE'] = t.LATITUDE.round(0).astype(int)
t['LONGITUDE'] = t.LONGITUDE.round(0).astype(int)

jan1_temps = t.groupby(['LATITUDE', 'LONGITUDE']).mean().unstack()
# There is a bad value of 3k stuck in there
jan1_temps[jan1_temps > 60] = 55
coldest = jan1_temps.min().min()
jan1_temps[:] = jan1_temps - coldest
warmest = jan1_temps.max().max()
jan1_temps[:] = jan1_temps / warmest
jan1_temps.to_pickle('data/temp_grid.pkl')
```
