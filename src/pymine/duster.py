import requests
from bs4 import BeautifulSoup
import pandas as pd
from pymine.create_id import create_id

def duster(urls):
    """
    Prepares a pandas dataframe by webscraping raw text from a list of urls ready to be input into a machine learning model.
    
    Parameters
    ----------
    urls: list
        list of target urls as strings

    Returns
    ----------
    df: pandas dataframe
        A dataframe with the webpage identifiers as a index, the raw url, and the raw text from the webpage with extra line breaks removed.
        
    Examples
    ----------
    >>> from pymine.duster import duster
    >>> duster(['https://www.cnn.com/world', 'https://www.foxnews.com/world', 'https://www.cbc.ca/news/world'])
                                        url                                           raw_text
    id
    cnn1          https://www.cnn.com/world   World news - breaking news, video, headlines ...
    foxnews1  https://www.foxnews.com/world  World | Fox NewsFox News   U.S.PoliticsMediaOp...
    cbc1      https://www.cbc.ca/news/world  World - CBC NewsContentSkip to Main ContentAcc...         
    """

    output = {}
    for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        output[url] = soup.text
    #create Dataframe from dictionary output of text_from_url()
    df = pd.DataFrame.from_dict(output, orient='index', columns=["raw_text"]).reset_index().rename(columns={"index":"url"})
    
    #remove line breaks
    df['raw_text'] = df['raw_text'].str.replace("\n", "")
    
    #add id as index
    df['id'] = create_id(df['url'].tolist())
    df = df.set_index('id')
    
    return df
    

