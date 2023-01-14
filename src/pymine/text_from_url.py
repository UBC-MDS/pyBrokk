def text_from_url(urls):
    """
    This function takes a list of URLs and returns the raw text as scraped from the URL using Beautiful Soup

    Parameters
    ----------
        urls: list
            List of URLs to scrape as strings
    
    Returns
    -------
    texts: dataframe
        Dataframe containing the url and raw text output as columns

    Examples
    --------

    >>> from pymine import text_from_url
    >>> url_list = ['https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html', 
    'https://realpython.github.io/fake-jobs/jobs/historic-buildings-inspector-conservation-officer-25.html', 
    'https://realpython.github.io/fake-jobs/jobs/back-end-web-developer-python-django-60.html']

    >>> text_from_url(url_list)

                            url                                                                                  | text
    0   https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html                                 Fake Python Fake Jobs for Your Web Scraping Journey Senior Python Developer Payne, Roberts and Davis Professional asset web application environmentally friendly detail-oriented asset. Coordinate educational dashboard agile employ growth opportunity. Company programs CSS explore role. Html educational grit web application. Oversea SCRUM talented support. Web Application fast-growing communities inclusive programs job CSS. Css discussions growth opportunity explore open-minded oversee. Css Python environmentally friendly collaborate inclusive role. Django no experience oversee dashboard environmentally friendly willing to learn programs. Programs open-minded programs asset. Location: Stewartbury,AAPosted: 2021-04-08
    1   https://realpython.github.io/fake-jobs/jobs/historic-buildings-inspector-conservation-officer-25.html      Fake Python Fake Jobs for Your Web Scraping Journey Historic buildings inspector/conservation officer Smith LLC Heavy church nature. Civil single city quite. Foreign agency when personal huge difficult player forget. Goal clear inside guy north. North add us accept hope soon. Location: North Brandonville, AP Posted: 2021-04-08
    2   https://realpython.github.io/fake-jobs/jobs/back-end-web-developer-python-django-60.html                   Fake Python Fake Jobs for Your Web Scraping Journey Back-End Web Developer (Python, Django) Stewart-Alexander Explore professional teamwork software developer dashboard distributed. Css asset distributed curious inclusive CSS. Professional motivated remote. Oversea web application Flask HTML CSS web application Java. Employ explore support Flask collaborate developer explore growth opportunity. Location: South Kimberly, AA Posted: 2021-04-08
    """
    # text_from_url code goes here...