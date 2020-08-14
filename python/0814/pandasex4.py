'''
Created on 2020. 8. 14.
@author: GDJ24
pandasex4.py : pandas 부분 선택 예제
'''

import pandas as pd

infile = "supplier_data.csv"
outfile = "pandas_out4.csv"

df = pd.read_csv(infile)
df_inset = df.loc[df["Invoice Number"].str.startswith("920-")]

print(df_inset)
df_inset.to_csv(outfile,index=False)

'''
   Supplier Name Invoice Number  Part Number     Cost Purchase Date
8     Supplier Z       920-4803         3321  $615.00        2/3/14
9     Supplier Z       920-4804         3321  $615.00       2/10/14
10    Supplier Z       920-4805         3321  $615.00       2/17/14
11    Supplier Z       920-4806         3321  $615.00       2/24/14
'''