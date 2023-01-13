def count_words(urls, words):
    """
    Counts the occurence of a specific list of words on a series of webpages
    
    Parameters
    ----------
    urls: list
        list of target urls as strings
    words: list
        List of target words as strings
        
    Returns
    ----------
    counts: dataframe
        A dataframe with the webpage identifiers as a index, target words as columns, and the counts of target words for each webpage
        
    Examples
    ----------
    >>> from pymine import count_words
    >>> count_words(['https://www.cnn.com/world', 'https://www.foxnews.com/world', 'https://www.cbc.ca/news/world'], ['tsunami', 'hurricane', 'earthquake', 'disaster'])
            tsunami hurricane earthquake disaster
    cnn1        0       3           0           1
    foxnews1    0       6           0           9
    cbc1        5       1           0           3          
    """
    # count_words code goes here...