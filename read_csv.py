import urllib2
import urllib
import sys
import base64
import json
import numpy as np
import pandas as pd


df = pd.read_csv('my_data_small.csv')
df.head()
#print "hello world!"
#print df
pd.set_option('display.width', pd.util.terminal.get_terminal_size()[0])
with pd.option_context('display.max_rows', 999, 'display.max_columns', 8):
	print df

