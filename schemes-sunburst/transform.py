'''
Cleansing & transforming CBGA budget data
===

AUTHOR: Suhas, github.com/jargnar
LICENSE: MIT
'''
import sys
import pandas as pd


def flatten(df):
    '''Transforms a file based on transformations.md'''
    # drop everything which does not have Index
    df = df.dropna(subset=['Index'], how='all')

    # create (level - 1) parent columns
    # TODO: cleverly compute levels automatically
    levels = 4
    for l in range(levels - 1, 0, -1):
        df['parent{}'.format(l)] = pd.Series([pd.np.nan] * len(df))

    # clever hierarchy traversal thing
    for level in range(levels, 1, -1):
        filt = df.Index.str.split('.').apply(lambda x: len(x) == level)
        indices = df[filt]['Index']
        for i in indices:
            # Get parent for index
            parts = i.split('.')
            for p in range(len(parts) - 1, 0, -1):
                par = '.'.join(parts[:p])
                if p == 1:
                    par = par + '.'
                par = df[df['Index'] == par]['Scheme Name'].iloc[0]
                df.loc[df['Index'] == i, 'parent{}'.format(p)] = par

    # drop the parents
    # (those that do not have budget details)
    df = df.dropna(subset=['Budget 2013-2014 Plan'], how='all')

    # everyone has parents
    # top most schemes are their own parents
    for l in range(2, levels):
        col = 'parent{}'
        df[col.format(l)] = df[col.format(l)].fillna(df[col.format(l - 1)])

    # lazy to write a better line, this will do for now
    df = df.replace('...', 0).replace('... ', 0)
    # save the results, phew
    df.to_csv(sys.argv[1] + '.clean.csv', index=False)

if __name__ == '__main__':
    flatten(pd.read_csv(sys.argv[1]))
