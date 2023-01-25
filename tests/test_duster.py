from pyBrokk.duster import duster
import pandas as pd

def test_duster():
    """
    Test input and output for duster() function
    
    Example
    ---------
    >>> test_duster()
    """
    
    urls = ['https://www.reddit.com/r/nba/', 'https://www.reddit.com/r/nfl/', 'https://vancouver.craigslist.org/search/apa', 'https://www.kijiji.ca/b-real-estate/richmond-bc/c34l1700288']
    actual = duster(urls)

    
    "Confirms the input is a list and all items in the list are strings"
    assert type(urls) is list and all(isinstance(item, str) for item in urls) == True, "Input is not a list of strings"
    
    "Confirms the output is a DataFrame"
    assert isinstance(actual, pd.DataFrame) == True, "Output is not a DataFrame"
    
    "Confirms the output number of rows is correct"
    assert len(actual) == len(urls), "Output contains an incorrect number of rows."
    
    "Confirms the output number of columns is correct"
    assert len(actual.columns) == 2, "Output contains an incorrect number of columns"