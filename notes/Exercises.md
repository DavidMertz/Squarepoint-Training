# NumPy

# Pandas

## Module 4, Processing

### Elevation

The NOAA temperature dataset does not seem to contain metadata indicating the 
units for ELEVATION.  But only one station is above 3500 *something*:

```python
temperatures.loc[temperatures.ELEVATION > 3500, ['LATITUDE', 'LONGITUDE']]
```

That station is at 46.55° N by 7.983333° E.  This is a location close to 
Lauterbrunnen, Switzerland, which is 2631ft == 802m.  This makes it likely
that the 3576 is feet.  But there *are* peaks in the Swiss up to 4634m, so 
it isn't as definite as we might want without knowing the station.

Probing further, if we assume the location is accurate within one minute of 
latitude, the tallest peak within about 2 km is about 2500m; so that would 
seem to exclude a station on a peak in meters.

Other approaches to narrowing this unit likely exist.

# Matplotlib

## Module 1, Guidelines

### Population

One hope we have, even though we deliberately did not mention it in the training 
material, is that students will arrive at the benefit of using log scale for
long time-scale population numbers.