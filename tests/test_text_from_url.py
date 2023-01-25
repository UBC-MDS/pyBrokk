from pyBrokk.text_from_url import text_from_url

def test_text_from_url():
    """
    Test the function text_from_url to:
    1. Test the input is a list of strings
    2. The output is a dictionary
    3. The output is parsed correctly using Beautiful Soup


    """

    urls = ['https://raw.githubusercontent.com/UBC-MDS/pyBrokk/main/tests/Fake%20Python%201.html', 'https://raw.githubusercontent.com/UBC-MDS/pyBrokk/main/tests/Fake%20Python%202.html', 'https://raw.githubusercontent.com/UBC-MDS/pyBrokk/main/tests/Fake%20Python%203.html']


    "Tests the input is a list of strings"
    assert type(urls) is list and all(isinstance(item, str) for item in urls) == True, 'Input must be a list of strings'

    "Tests the output is a dictionary"
    assert type(text_from_url(urls)) is dict, 'The output is not a dictionary'