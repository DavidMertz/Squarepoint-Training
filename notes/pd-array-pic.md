```python
import numpy as np
import pandas as pd

arr = np.linspace(1, 24, 24).reshape(4, 6)
df = pd.DataFrame(arr)

df.applymap("{0:.1f}".format).style.set_properties(
    **{'background-color': 'black',
       'color': 'lawngreen',
       'border-color': 'white',
       'font-size': '12pt'})
```

