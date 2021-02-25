# cornerstone libraries
import pandas as pd
import numpy as np
# data viz libraries
import matplotlib.pyplot as plt
import seaborn as sns

#* importing libraries inside Jupyter notebook
# # importing python files inside a jupyter notebook is tricky. 
# import sys  
# sys.path.insert(0, '/home/henri/Documents/Post Lighthouse-Lab work/streamlitWebsiteCVProject/projects')

# from customPandas import *

#* improting libraries inside a python file


#* pandas specific EDA functions
def totalPercentageNullData(df, threshold=0):
    """
    input:
        df = any Pandas DataFrame.
        threshold = cut-off number for displaying missing val. Default is 0
    output: 
        DF with 2 features [count of missing val, their weight]
    """
    total = df.isnull().sum().sort_values(ascending=False)
    percent = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat([total, percent*100], axis=1, keys=['Total', 'Percent'])

    if threshold >100:
        print(f'threshold value set to: {threshold}. Please select between 0% and 100% ')
        return

    return missing_data[missing_data > threshold].dropna()

def correlationHeatmap(df,filterFeature=0,half=False):
    """
    input:
        df = Pandas DataFrame
        filter = [feature,threshold]
    output:
        None
        plot heatmap
    requirements:
    notes:
        taken from https://towardsdatascience.com/why-feature-correlation-matters-a-lot-847e8ba439c4
        the corr map already filter out any non numeric values
    """

    correlations = df.corr()
    if filterFeature:
        resultFeature = correlations.index[abs(correlations[filterFeature[0]])>filterFeature[1]]
        correlations = df[resultFeature].corr()
    fig, ax = plt.subplots(figsize=(10,10))

    # we do not want duplicate (triangle)    
    if half:
        # Generate a mask for the upper triangle
        mask = np.triu(np.ones_like(correlations, dtype=bool))
        sns.heatmap(correlations,mask=mask, vmax=1.0,cbar=False, center=0, fmt='.2f',
                square=True, linewidths=.5, annot=True, cbar_kws={"shrink": .70})
    else:
        sns.heatmap(correlations, vmax=1.0,cbar=False, center=0, fmt='.2f',
                square=True, linewidths=.5, annot=True, cbar_kws={"shrink": .70})
    plt.show()

#! works well now, but most likely will not fit every situation
def pandasExploratoryData(data,desiredDtypes,uniqueValueShown=5,stringTruncatedVal=75,brief=True):
    """
    input:
        data = any Pandas DataFrame
        uniqueValueShown = How many unique value you want displayed
        stringTruncatedVal = value where we will truncate anything past
        desiredDtypes = ['cat', 'num', 'gen', 'missing','corr']
        brief = shortcut to not
    output:
        none
        print all required info
    functions that print basic information depending on the user's choice

    reasoning behind this function: Basic EDA is often a tedious set of instruction to get a clear ide
    """

    # We are not interrestd with bools   
    catVariables = data[data.dtypes[(data.dtypes == 'object')].index.tolist()]
    #! improvement numVar to be any columns not in catVariable
    numVariables = data[data.dtypes[(data.dtypes == 'float') | (data.dtypes == 'int')].index.tolist()]
    # introduction statement
    print(f'Only printing the first {uniqueValueShown} unique variables and {stringTruncatedVal} chars')
    # the multiple if is not the most elegant method, but its simplicity makes it easy
    # only displays objects dtype
    if 'cat' in desiredDtypes:
        print('\nCategorical variables --------------------------------------------\n')
        for cat in catVariables.columns.tolist():
            print(f'\nThere are {data[cat].nunique()} unique val for {cat}')
            
            if not brief:

                for index,uniqueCat in enumerate(data[cat].unique()[:uniqueValueShown]):
                    # handling out of index error because the uniqueVal is shorter than the truncated value
                    if len(uniqueCat) < stringTruncatedVal:
                        print(f'{index}. {uniqueCat}')

                    else:
                        print(f'{index}. {uniqueCat[:stringTruncatedVal]}')
    # only display float/int(64)
    if 'num' in desiredDtypes:
        print('\nNumerical variables --------------------------------------------\n')
        for num in numVariables.columns.tolist():
            print(f'There are {data[num].nunique()} unique {num}')
            print(f'The median is  {data[num].median()}, mean {data[num].mean()}\n')
            # brief flag to enumerate unique values
            if not brief:
                for index,uniqueNum in enumerate(data[num].unique()[:uniqueValueShown]):
                    print(f'{index}. {uniqueNum}')

    #basic pandas EDA commands
    if 'gen' in desiredDtypes:
        print('\nBasic information --------------------------------------------\n')
        print(f'\ndata info:\n{data.info()}')
        print(f'\ndata description:\n{data.describe()}')
        print(f'\ndata shape:\ncolumns {data.shape[0]} rows: {data.shape[1]}')

    # threshold has been set to 0 for all missing values
    if 'missing' in desiredDtypes:
        print('\nMissing/Null Data --------------------------------------------\n')
        print(totalPercentageNullData(data))
    
    if 'corr' in desiredDtypes:
        print('\nCorrelation triangle heatmap --------------------------------------------\n')
        correlationHeatmap(data,half=True)

#* Scikit-learn 
class ToDenseTransformer():
    """
    class instance called 
    """
    def transform(self, X, y=None, **fit_params):
        """
        
        """
        return X.todense()

    # just return self
    def fit(self, X, y=None, **fit_params):
        return self