from flask import Flask, request, jsonify
import pandas as pd
from sklearn.externals import joblib

best_perf_model = joblib.load()

# Set of prediction functions that expect
# a singular |patient_data| in the form of Index or pd.df
# and returns boolean:
# True for LOS >= 4
# False for LOS <= 3

# predict using full feature model
def full_predict(patient_data):
    los = True
    return los

# predict using sparse model
def sparse_predict(patient_data):
    los = True
    return los

# predict using hybrid model
def hybrid_predict(patient_data):
    los = True
    return los

# predict using neural net model
def nn_predict(patient_data):
    los = True
    return los

# predict using current best performing model
def bm_predict(patient_data):
    los = True
    return los

# trains selected model on given data
# manual selection of features optional
def train(data,model_type,selection,perf_metrics):
    data = df_transform(data)

    if(selection):
        data = feature_reduce(data,selection)
    if(model_type = "sparse"):
        generate_sparse_model(data)
    else if(model_type = "hybrid"):
        generate_hybrid_model(data)
    else if(model_type = "nn"):
        generate_nn(data)
    else if(model_type = "best"):
        generate_best_model(data,perf_metrics)
    else:
        print 'one of your inputs is wrongly formatted'

# generates selected model based on given model_type request
# Note to reader: These functions are currently being tested in notebooks
# Implementation is a simple copy and paste
def generate_full_model(data):
    return pickle
def generate_sparse_model(data):
    return pickle
def generate_hybrid_model(data):
    return pickle
def generate_nn(data):
    return pickle
def generate_best_model(data,perf_metrics):
    return pickle

# Reduces a dataset using set of feature reduction techniques
# |data| is pd.df form of raw data
# |selection| is Index of additional manual selections
# |reduced| is pd.df of data with with reduced featureset
def feature_reduce(data,selection):

    reduced = []
    # feat_ranking is an array of arrays
    # in key-value form
    # ['Technique',['feature',performance_score]]
    # example feat_ranking = ['PCA',['Age', 0.7]]
    feat_ranking = [['PCA',0],[]]

    technique_usage = feature_selection_technique_eval(feat_ranking)

    # Thomas is working on
    return reduced

# Expects feat_ranking as described in feature_reduce
# returns array of best performing feature reduction techniques
# Ex. ['PCA','LinSVM']
def feature_selection_technique_eval(feat_ranking):
    return []

# Expects dataset in pd.df form
# Expects perf_metrics in Index
# ['Type 1': Cost, 'Type 2': Cost]
# Runs full,sparse,hybrid,and neural net models
# Evaluates model performance against perf_metrics supplied
# returns best model stored as .pkl
# Warning: calling this function takes a long time
def generate_best_model(data,perf_metrics):

# Identifies dataset format
# Coerces dataset into usable pd.df
def df_transform(data):
