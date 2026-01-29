# 2878. Get the Size of a DataFrame

## Problem
Given a pandas DataFrame `players` with information about players (columns like `player_id`, `name`, `age`, `position`, etc.), return the size of the DataFrame as an array `[number of rows, number of columns]`.

---

## Solution

We can use the `.shape` attribute of a pandas DataFrame.  

- `players.shape` returns a tuple `(number_of_rows, number_of_columns)`.  
- We can unpack it and return it as a list.

### Python Implementation
 ```python  
import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    num_rows, num_cols = players.shape
    return [num_rows, num_cols]
```

### Example Usage

```python
df = pd.DataFrame({
    'player_id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 22],
    'position': ['Forward', 'Midfield', 'Defender']
})
```

print(getDataframeSize(df))  # Output: [3, 4]




