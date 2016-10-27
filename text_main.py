import sys
import numpy as np
import pandas as pd


from azure_ml import azureml_main

df = pd.read_csv('my_data_small.csv')
df2 = df
pd.set_option('display.width', pd.util.terminal.get_terminal_size()[0])
with pd.option_context('display.max_rows', 999, 'display.max_columns', 8):
        print df

azureml_main("2745e7fb392b480e95d4df7ebc4b3b85", "https://westus.api.cognitive.microsoft.com/", df, df2)

print "----\n Output dataFrame \n"
with pd.option_context('display.max_rows', 999, 'display.max_columns', 8):
        print df2


