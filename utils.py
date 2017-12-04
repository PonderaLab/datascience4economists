# -*- coding: utf-8 -*-
import argparse
import os
from os.path import expanduser, exists, join
import pandas as pd
import numpy as np
from unidecode import unidecode_expect_nonascii as ud
import functools as tools


#  # Pondera libraries & vars
PATH_PONDERA = join(expanduser('~'), 'Pondera')
PATH_D4E = join(*[PATH_PONDERA, 'playground', 'data4eco_itam'])


def get_parser():
    """Get parser for command line arguments."""
    description = ("Utils for the *data4eco* course."
                   ""
                   "Run handy commands for administering the files & stuff of the course."
                   "- alumnifolders: Organize alumni folders.")
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('do',
                        help='The command to execute')
    return parser


def makefolders(root_dir, subfolders):
    concat_path = tools.partial(join, root_dir)
    map(os.makedirs, map(concat_path, subfolders))


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    if args.do == 'alumnifolders':
        PATH = join(PATH_D4E, 'alumni')
        list_file = join(PATH, 'alumnilist.xlsx')
        if exists(list_file):
            df = pd.read_excel(list_file, dtype={'cu': 'object',
                                                 'name': 'object', 'surname': 'object'})
            for i, r in df.iterrows():
                if (not pd.isnull(r['name'])) and (not pd.isnull(r['surname'])):
                    fname = '_'.join([str(r['cu']), ud(r['name'].split(' ')[0]),
                                      ud(r['surname'].split(' ')[0])])
                    print(fname)
                    try:
                        os.mkdir(join(PATH, fname))
                    except Exception as e:
                        print('Ya existe el directorio ' + fname)
