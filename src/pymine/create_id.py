def create_id(urls):
    """
    Convert a list of provided urls into a list of unique identifiers for use in downstream functions
    
    Parameters
    ----------
    urls: list
        A list of urls as strings
        
    Returns
    ----------
    ids: list
        A list of unique identifiers as strings
        
    Examples
    ----------
    >>> from pymine import create_id
    >>> create_id(['https://www.reddit.com/r/nba/', 'https://vancouver.craigslist.org/search/apa', 'https://www.kijiji.ca/b-real-estate/richmond-bc/c34l1700288'])
    ['reddit1', 'craigslist1', 'kijiji1']
    """
    # create_id code goes here...