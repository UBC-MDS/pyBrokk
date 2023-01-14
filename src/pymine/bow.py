def bow(urls, text):
    """
    Converts a raw text to a list of target words as strings
    
    Parameters
    ----------
    urls : list
        list of url id's as string
    
    text : str
        list of extracted text from each web page. 
           
    Returns
    ----------
    bag_of_words : dataframe
        dataframe with the webpage id's (string) and bag of words of the webpage's text (dictionary)  
        
    Examples
    ----------
    >>> urls = ['https://www.cnn.com/world', 'https://www.foxnews.com/world', 'https://www.cbc.ca/news/world']
    >>> text = ["This is CNN!", "This is Foxnews!", "According to news, This is cbc news!"] 
    >>> bow(urls, text)
    URL          BOW 
    ---          ---     
    cnn1        {"this": 1, "is" : 1, "cnn" : 1 }
    foxnews1    {"this": 1, "is" : 1, "foxnews" : 1 }
    cbc1        {"according": 1, "to": 1, "news" : 2, "this": 1, "is":1, "cbc" : 1}
 
    """
    # count_words code goes here...