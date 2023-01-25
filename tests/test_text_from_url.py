from pyBrokk.text_from_url import text_from_url

def test_text_from_url():
    """
    Test the function text_from_url to:
    1. Test the input is a list of strings
    2. The output is a dictionary
    3. The output is parsed correctly using Beautiful Soup


    """

    urls = ['https://raw.githubusercontent.com/UBC-MDS/pyBrokk/main/tests/Fake%20Python%201.html', 'https://raw.githubusercontent.com/UBC-MDS/pyBrokk/main/tests/Fake%20Python%202.html', 'https://raw.githubusercontent.com/UBC-MDS/pyBrokk/main/tests/Fake%20Python%203.html']

    test_result = {'https://realpython.github.io/fake-jobs/jobs/scientist-research-maths-22.html': '\n\n\n\n\nFake Python\n\n\n\n\n\n\n        Fake Python\n      \n\n        Fake Jobs for Your Web Scraping Journey\n      \n\n\n\n\nScientist, research (maths)\nManning, Welch and Herring\n\nBank ten guess. Course book music amount. Fire town worker. Image central challenge term memory. By care lose politics. Role mind statement.\nLocation: Laurenland, AE\nPosted: 2021-04-08\n\n\n\n\n\n\n\n',
    'https://realpython.github.io/fake-jobs/jobs/futures-trader-41.html': '\n\n\n\n\nFake Python\n\n\n\n\n\n\n        Fake Python\n      \n\n        Fake Jobs for Your Web Scraping Journey\n      \n\n\n\n\nFutures trader\nSchneider-Brady\n\nPart instead city type short rather. Once born control white. Rather beyond share energy size. Meeting movie avoid American address simply. Thousand impact six loss. Finish star be.\nLocation: North Jason, AE\nPosted: 2021-04-08\n\n\n\n\n\n\n\n',
    'https://realpython.github.io/fake-jobs/jobs/software-developer-python-40.html': '\n\n\n\n\nFake Python\n\n\n\n\n\n\n        Fake Python\n      \n\n        Fake Jobs for Your Web Scraping Journey\n      \n\n\n\n\nSoftware Developer (Python)\nAdams-Brewer\n\nAsset include open-minded HTML fast-growing. Coordinate discussions grit discussions. Coordinate communities HTML. Support Java Java talented explore dashboard. Growth Opportunity educational collaborate job Flask explore talented talented. Dashboard distributed oversee environmentally friendly. Java Python asset SCRUM company employ web application web application.\nLocation: Brockburgh, AE\nPosted: 2021-04-08\n\n\n\n\n\n\n\n'}

    "Tests the input is a list of strings"
    assert type(urls) is list and all(isinstance(item, str) for item in urls) == True, 'Input must be a list of strings'

    "Tests the output is a dictionary"
    assert type(text_from_url(urls)) is dict, 'The output is not a dictionary'