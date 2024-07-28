# NumPy

## Numpy-1_Arrays_Dtypes_Shapes

Create 3-D array with specified values.
```
arr_odd_3d = np.arange(17, 100, 2).reshape((2, 3, 7))
```

Complex number version.
```
np.arange(17, 100, 2, dtype=np.complex64).reshape((2, 3, 7))
```

Array reshaping
```
# Create the array...
arr_odd_3d = np.arange(17, 100, 2).reshape((2, 3, 7))

# View as 2-D...
arr_odd_2d = arr_odd_3d.reshape((6, 7))
print(arr_odd_2d)

# Change the values in the corners...
arr_odd_2d[(0, 0)] = 0
arr_odd_2d[0, -1] = 0
arr_odd_2d[-1, 0] = 0
arr_odd_2d[-1, -1] = 0
print(arr_odd_2d)

# Determine the offsets into 1-D view...
arr_odd_1d = arr_odd_2d.reshape(42)
print(np.where(arr_odd_1d == 0))

# Determine the offsets into 3-D view
print(np.where(arr_odd_3d == 0))

# The parallel arrays of dimension indices is useful, 
# but could be confusing at first. We can also look at:
print(np.array(list(zip(*np.where(arr_odd_3d == 0)))))
print(arr_odd_3d)
```

Fill arrays with radian values.
```
from math import tau, pi
rng = np.random.default_rng()

# Array of radians
# Old style: np.random.uniform(0., 2 * np.pi, 400)
arr_rad = rng.uniform(0, tau, 400)

# 2-D array of quadrants
arr_quads = np.array(
    [
        rng.uniform(0, pi/2, 100), 
        rng.uniform(pi/2, pi, 100),
        rng.uniform(pi, 1.5 * pi, 100),
        rng.uniform(1.5 * pi, tau, 100)
    ]
)

# Extra: Column quadrants
# The "cheat" is easiest
arr_col_quads = arr_quads.T

# Without transposition:
arr_col_quads = np.column_stack(
    (
        rng.uniform(0, pi/2, 100), 
        rng.uniform(pi/2, pi, 100),
        rng.uniform(pi, 1.5 * pi, 100),
        rng.uniform(1.5 * pi, tau, 100)
    )
)
```

Colors in locations
```
# Colors
RED, GREEN, BLUE = 1, 2, 3
rng = np.random.default_rng()

# Cube of colors
# Old-style: np.random.randint(1, 4, (3, 3, 3))
arr_colors = rng.integers(1, 4, (3, 3, 3))

# Diagonal of colors
arr_diag = np.diag(rng.integers(1, 4, (5,)))

# Extra: Distinct numbers, random order
arr_rand_ord = np.arange(1, 101)
rng.shuffle(arr_rand_ord)

# Extra: Poisson distribution
arr_poisson = rng.poisson(size=(20, 20))
```

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