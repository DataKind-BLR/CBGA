import argparse
import os
import pandas as pd
from transform import flatten
from sequences import sequences


def process_budget_files():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="Path to the input folder")
    args = vars(ap.parse_args())
    path_to_files = args['input']

    for subdir, dirs, files in os.walk(path_to_files + '/input'):
        for file in files:
            if file != '.DS_Store':
                try:
                    flatten(pd.read_csv(subdir+'/'+file, error_bad_lines=False), path_to_files+'/output/'+file.split('.')[0])
                except:
                    print file

def sequencify_files():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="Path to the input folder")
    args = vars(ap.parse_args())
    path_to_files = args['input']
    for subdir, dirs, files in os.walk(path_to_files + '/output'):
        for file in files:
            if file != '.DS_Store':
                try:
                    sequences(pd.read_csv(subdir+'/'+file, error_bad_lines=False), path_to_files+'/output/'+file.split('.')[0])
                except:
                    print file

if __name__ == '__main__':
    process_budget_files()
    sequencify_files()
