'''
Converts df to d3 sequences sunburst format
===

AUTHOR: Suhas, github.com/jargnar
LICENSE: MIT
'''
import sys
import pandas as pd
from slugify import slugify

def removenan(s):
    while 'nan' in s:
        s.remove('nan')

    return '|'.join(s)


def sequences(df, filename="out"):
    '''Sequences routine to convert to sequences.csv'''
    # slug = slugify(to_lower=True)
    s, c = 'sequences', [df.columns[5], df.columns[8], df.columns[11]]
    df[s] = pd.Series([])
    
    for i, row in df.iterrows():
        df.loc[i, s] = slugify(unicode(row.parent1))
        if row.parent1 != row.parent2:
            df.loc[i, s] = df.loc[i, s] + '|' + slugify(unicode(row.parent2))
        if row.parent2 != row.parent3:
            df.loc[i, s] = df.loc[i, s] + '|' + slugify(unicode(row.parent3))
        if row.parent3 != row['Scheme']:
            df.loc[i, s] = df.loc[i, s] + '|' + slugify(unicode(row['Scheme']))

    df[s] = df[s].astype(str)
    df[s] = df[s].str.split('|').apply(removenan)
    df1 =  df[df[c] > 0][c]
    df1.index = df[s]
    df1 = df1.replace('nan', 0)
    df1.to_csv(filename + '.sequences.csv')


if __name__ == '__main__':
    sequences(pd.read_csv(sys.argv[1]))
