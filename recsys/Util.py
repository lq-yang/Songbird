# -*- coding: UTF-8 -*-

import os
import pandas as pd

def prepare_data(path, encoding, index_col, header):
    """
    :param path: file path
    :param encoding: encoding type
    :param index_col: index columns
    :param header: header index
    :return: all the data to prepare and store in memory
    """
    file_path = pd.read_csv(path, encoding=encoding, header=header)
    cols = file_path.columns
    res = {}
    for index, row in file_path.iterrows():
        f = row[cols[0]]
        p = row[cols[1]]
        res[f] = pd.read_csv(p, encoding=encoding, index_col=index_col, header=header)
        print "**** load data " + f
    return res

if __name__ == '__main__':
    dir_path = os.path.dirname(__file__)
    file_path = dir_path + "/" + "../data/data_path.csv"
    encoding = "utf-8"
    index_col = 0
    header = 0
    res = prepare_data(path=file_path, encoding=encoding, index_col=index_col, header=header)
