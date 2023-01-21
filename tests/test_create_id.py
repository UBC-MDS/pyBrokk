from pymine.create_id import create_id

def test_create_id():
    """
    Test input and output for create_id() function
    
    Example
    ---------
    >>> test_create_id()
    """
    
    urls = ['https://www.reddit.com/r/nba/', 'https://www.reddit.com/r/nfl/', 'https://vancouver.craigslist.org/search/apa', 'https://www.kijiji.ca/b-real-estate/richmond-bc/c34l1700288']
    expected = ["reddit1", 'reddit2', 'craigslist1', 'kijiji1']
    actual = create_id(urls)

    
    "Confirms the input is a list and all items in the list are strings"
    assert type(urls) is list and all(isinstance(item, str) for item in urls) == True, "Input is not a list of strings"
    
    "Confirms the output is a list and all items in the list are strings"
    assert type(actual) is list and all(isinstance(item, str) for item in actual) == True, "Output is not a list of strings"
    
    "Confirms the output list of identifiers is the same length as the input list of urls"
    assert len(actual) == len(urls), "Input and Output sizes do not match"
    
    "Confirms all identifiers are unique and no duplicates were generated"
    assert len(set(actual)) == len(actual), "Output contains duplicate identifiers"
    
    "Confirms the actual output matches the expected output of the function"
    assert actual == expected, "URL identifiers created incorrectly"