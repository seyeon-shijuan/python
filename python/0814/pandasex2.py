'''
Created on 2020. 8. 14.
@author: GDJ24
pandasex2.py : pandas를 이용하여 csv 파일 읽기
'''

import pandas as pd

infile = "CCTV_guro.csv"
outfile = "pandas_out2.csv"
df = pd.read_csv(infile,encoding="UTF8")
print(df)


'''
        관리기관명                소재지도로명주소  ...          경도     데이터기준일자
0  서울특별시 구로구청     서울특별시 구로구 고척로45길 39  ...  126.853278  2020-04-27
1  서울특별시 구로구청     서울특별시 구로구 고척로45길 39  ...  126.853278  2020-04-27
2  서울특별시 구로구청     서울특별시 구로구 고척로45길 39  ...  126.853278  2020-04-27
3  서울특별시 구로구청   서울특별시 구로구 개봉로3가길 88-9  ...  126.851814  2020-04-27
4  서울특별시 구로구청        서울특별시 구로구 구일로 68  ...  126.873473  2020-04-27
5  서울특별시 구로구청        서울특별시 구로구 구일로 62  ...  126.874362  2020-04-27
6  서울특별시 구로구청  서울특별시 구로구 구로중앙로27가길 23  ...  126.886050  2020-04-27
7  서울특별시 구로구청  서울특별시 구로구 구로중앙로27나길 18  ...  126.884902  2020-04-27
8  서울특별시 구로구청    서울특별시 구로구 가마산로26길 34  ...  126.891586  2020-04-27
9  서울특별시 구로구청    서울특별시 구로구 가마산로27길 69  ...  126.889765  2020-04-27

[10 rows x 13 columns]
'''

print(df["경도"])
'''
0    126.853278
1    126.853278
2    126.853278
3    126.851814
4    126.873473
5    126.874362
6    126.886050
7    126.884902
8    126.891586
9    126.889765
Name: 경도, dtype: float64
'''