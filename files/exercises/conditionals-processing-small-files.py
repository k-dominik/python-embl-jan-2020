# Processing Small Files

# Modify this program so that it only processes files with fewer than 50 records.

import glob
import pandas as pd
for filename in glob.glob('data/*.csv'):
    contents = pd.read_csv(filename)
    ____:
        print(filename, len(contents))
