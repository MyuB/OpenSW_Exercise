import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(16).reshape((4,4)),
                    index=['q', 'w', 'e', 'r'],
                    columns=['a', 'b', 'c', 'd'])

print(data.iloc[:, :3][data.c > 5])