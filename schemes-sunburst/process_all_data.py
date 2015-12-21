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

    for subdir, dirs, files in os.walk(path_to_files):
        if subdir.split('/')[-1] != 'input' and subdir.split('/')[-1] != 'output' and subdir.split('/')[-1] != 'sequences':
            if not os.path.exists(os.getcwd()+'/'+subdir+'/output'):
                os.makedirs(os.getcwd()+'/'+ subdir+'/output')

        for _file in files:
            if _file != '.DS_Store':
                try:
                    # import pdb;pdb.set_trace() 
                    flatten(pd.read_csv(subdir+'/'+_file, error_bad_lines=False), '/'.join((os.getcwd()+'/'+subdir).split('/')[0:-1])+'/output/'+_file.split('.')[0])
                except:
                    print _file

def sequencify_files():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="Path to the input folder")
    args = vars(ap.parse_args())
    path_to_files = args['input']

    for subdir, dirs, files in os.walk(path_to_files):
        if subdir.split('/')[-1] != 'input' and subdir.split('/')[-1] != 'output' and subdir.split('/')[-1] != 'sequences':
            if not os.path.exists(os.getcwd()+'/'+subdir+'/sequences'):
                os.makedirs(os.getcwd()+'/'+ subdir+'/sequences')

        if subdir.split('/')[-1] == 'output':
            for _file in files:
                if _file != '.DS_Store':
                    try:
                        sequences(pd.read_csv(subdir+'/'+_file, error_bad_lines=False), '/'.join((os.getcwd()+'/'+subdir).split('/')[0:-1])+'/sequences/'+_file.split('.')[0])
                    except:
                        print _file

if __name__ == '__main__':
    # process_budget_files()
    sequencify_files()
