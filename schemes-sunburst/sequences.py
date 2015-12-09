'''
Converts df to d3 sequences sunburst format
===

AUTHOR: Suhas, github.com/jargnar
LICENSE: MIT
'''
import sys
import pandas as pd
from slugify import slugify


def sequences(df, filename="out"):
    '''Sequences routine to convert to sequences.csv'''
    # slug = slugify(to_lower=True)

    s, c = 'sequences', df.columns[5]
    df[s] = pd.Series([])
    for i, row in df.iterrows():
        df.loc[i, s] = slugify(unicode(row.parent1))
        if row.parent1 != row.parent2:
            df.loc[i, s] = df.loc[i, s] + '|' + slugify(unicode(row.parent2))
        if row.parent2 != row.parent3:
            df.loc[i, s] = df.loc[i, s] + '|' + slugify(unicode(row.parent3))
        if row.parent3 != row['Scheme']:
            df.loc[i, s] = df.loc[i, s] + '|' + slugify(unicode(row['Scheme']))

    df[df[c] > 0][[s, c]].to_csv(filename + '.sequences.csv', index=False, header=False)


if __name__ == '__main__':
    sequences(pd.read_csv(sys.argv[1]))
