# -*- coding: UTF-8 -*-
import os
import pandas as pd
import cPickle as pkl


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
        print "**** load data for " + f
    return res


def prepare_model(path):
    """
    :param path: model path
    :return: all the model that we use for classification
    """
    model_path = pd.read_csv(path)
    cols = model_path.columns
    res = {}
    for index, row in model_path.iterrows():
        m = row[cols[0]]
        p = row[cols[1]]
        res[m] = pkl.load(open(p, 'r'))
        print "*** prepare model for " + m
    return res


def prepare_all():
    """
    :return: retrun all the data and model prepared 
    """
    dir_path = os.path.dirname(__file__)
    file_path = dir_path + "/" + "../data/data_path.csv"
    model_path = dir_path + "/" + "../data/model_path.csv"
    ref_path = dir_path + "/" + "../data/ref_path.csv"
    encoding = "utf-8"
    index_col = 0
    header = 0
    data_res = prepare_data(path=file_path, encoding=encoding, index_col=index_col, header=header)
    model_res = prepare_model(model_path)
    return data_res, model_res
