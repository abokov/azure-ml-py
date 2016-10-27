import urllib2
import urllib
import sys
import base64
import json
import numpy as np
import pandas as pd

# The entry point function can contain up to two input arguments:
#   Param<dataframe1>: a pandas.DataFrame
#   Param<dataframe2>: a pandas.DataFrame
def azureml_main(account_key, base_url, dataframe1 = None, dataframe2 = None):

    # Execution logic goes here
    #print('Input pandas.DataFrame #1:\r\n\r\n{0}'.format(dataframe1))

# Account key is for Ted Way
    #account_key = str(dataframe2['Col1'][0])
    #account_key = 'api_key' 
    #print "Account key = ", account_key
    #exit

    #base_url = 'https://api.datamarket.azure.com/data.ashx/amla/text-analytics/v1'
    #base_url = str(dataframe2['Col2'][0])         
    #base_url = 'https://westus.api.cognitive.microsoft.com/'

    headers = {'Content-Type':'application/json', 'Ocp-Apim-Subscription-Key':account_key}

    #input_text = sys.argv[2]
    sentiment_scores = []
    num_examples = len(dataframe1.index)
    input_texts = '{"documents":['
#for each record
    for i in range(0,num_examples):
        input_text = str(dataframe1['Text'][i])           
        input_text = input_text.replace("\"", "'")

        #params = { 'Text': input_text}        
        input_texts = input_texts + '{"id":"' + str(i) + '","text":"'+ input_text + '"},'        

    input_texts = input_texts + ']}'
    print input_texts

    # Detect sentiment.
    batch_sentiment_url = base_url + 'text/analytics/v2.0/sentiment'        

    req = urllib2.Request(batch_sentiment_url, input_texts, headers) 
    response = urllib2.urlopen(req)
    result = response.read()
    obj = json.loads(result)

    for sentiment_analysis in obj['documents']:            
        sentiment_scores.append( str(sentiment_analysis['score']))  
        #print('Sentiment score: ' + str(obj['Score']))

    sentiment_scores = pd.Series(np.array(sentiment_scores))        

    df1 = pd.DataFrame({'SentimentScore':sentiment_scores})

# Don't return the original text'
    #frames = [dataframe1, df1]

    #dataframe1 = pd.concat(frames, axis=1)   

    # Return value must be of a sequence of pandas.DataFrame
    return df1


