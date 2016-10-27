import sys
import numpy as np
import pandas as pd
import azureml
from azureml import Workspace
from azureml import AzureMLHttpError
from azureml import services

dataset_name="airport dataset"
workspace_token='TzIx/lKiAd4xSvJy+LYSa9WnsoWJStEhjMXMqI3dVUh+ZBvJCONa3URdI5NX28JTg80IRJHqQqV7dac88QaDrA=='
workspace_id='868c4254da56465897d35db0af7beed2'

from azure_ml import azureml_main

dataframe = pd.read_csv('my_data_small.csv')
#df2 = df
pd.set_option('display.width', pd.util.terminal.get_terminal_size()[0])
with pd.option_context('display.max_rows', 999, 'display.max_columns', 8):
        print dataframe

workspace = Workspace(workspace_id, workspace_token)

datasets_arr = []
i=0
for ds in workspace.datasets:
#    print(ds.name, " ", ds )
	datasets_arr.append( ds.name )
	i+=1

# --
# Update dataset from file 

#if dataset_name in datasets_arr
if [dataset_name in datasets_arr]:
	print "update dataset in Azure ML"
	dataset = workspace.datasets[dataset_name]
	dataset.update_from_dataframe(dataframe)
else:
	print "Add dataset into Azure ML"
	try:
	    workspace.datasets.add_from_dataframe(
        	dataframe,
	        azureml.DataTypeIds.GenericCSV,
	        dataset_name,
	        'Test data set - WW airport '
	    )
	except AzureMLHttpError as error:
		    print(error.status_code)
		    print(error)
		    exit()


# --
# Add our ML func

@azureml.services.publish(workspace_id, workspace_token)
@azureml.services.types(a = int, b = int)
@azureml.services.returns(int)
def func(a, b):
    return   a + b


