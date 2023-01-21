import requests
from bs4 import BeautifulSoup

def text_from_url(urls):
    """
    This function takes a list of URLs and returns the raw text as scraped from the URL using Beautiful Soup

    Parameters
    ----------
        urls: list
            List of URLs to scrape as strings
    
    Returns
    -------
    texts: dictionary
        Dictionary containing the url as keys and raw text output as values

    Examples
    --------
text_from_url(["https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html", "https://realpython.github.io/fake-jobs/jobs/energy-engineer-1.html"])

   {'https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html': <!DOCTYPE html>
 
 <html>
 <head>
 <meta charset="utf-8"/>
 <meta content="width=device-width, initial-scale=1" name="viewport"/>
 <title>Fake Python</title>
 <link href="https://cdn.jsdelivr.net/npm/bulma@0.9.2/css/bulma.min.css" rel="stylesheet"/>
 </head>
 <body>
 <section class="section">
 <div class="container mb-5">
 <h1 class="title is-1">
         Fake Python
       </h1>
 <p class="subtitle is-3">
         Fake Jobs for Your Web Scraping Journey
       </p>
 </div>
 <div class="container">
 <div class="columns is-multiline" id="ResultsContainer">
 <div class="box">
 <h1 class="title is-2">Senior Python Developer</h1>
 <h2 class="subtitle is-4 company">Payne, Roberts and Davis</h2>
 <div class="content">
 <p>Professional asset web application environmentally friendly detail-oriented asset. Coordinate educational dashboard agile employ growth opportunity. Company programs CSS explore role. Html educational grit web application. Oversea SCRUM talented support. Web Application fast-growing communities inclusive programs job CSS. Css discussions growth opportunity explore open-minded oversee. Css Python environmentally friendly collaborate inclusive role. Django no experience oversee dashboard environmentally friendly willing to learn programs. Programs open-minded programs asset.</p>
 <p id="location"><strong>Location:</strong> Stewartbury, AA</p>
 <p id="date"><strong>Posted:</strong> 2021-04-08</p>
 </div>
 </div>
 </div>
 </div>
 </section>
 </body>
 </html>,
 'https://realpython.github.io/fake-jobs/jobs/energy-engineer-1.html': <!DOCTYPE html>
 
 <html>
 <head>
 <meta charset="utf-8"/>
 <meta content="width=device-width, initial-scale=1" name="viewport"/>
 <title>Fake Python</title>
 <link href="https://cdn.jsdelivr.net/npm/bulma@0.9.2/css/bulma.min.css" rel="stylesheet"/>
 </head>
 <body>
 <section class="section">
 <div class="container mb-5">
 <h1 class="title is-1">
         Fake Python
       </h1>
 <p class="subtitle is-3">
         Fake Jobs for Your Web Scraping Journey
       </p>
 </div>
 <div class="container">
 <div class="columns is-multiline" id="ResultsContainer">
 <div class="box">
 <h1 class="title is-2">Energy engineer</h1>
 <h2 class="subtitle is-4 company">Vasquez-Davidson</h2>
 <div class="content">
 <p>Party prevent live. Quickly candidate change although. Together type music hospital. Every speech support time operation wear often.</p>
 <p id="location"><strong>Location:</strong> Christopherville, AA</p>
 <p id="date"><strong>Posted:</strong> 2021-04-08</p>
 </div>
 </div>
 </div>
 </div>
 </section>
 </body>
 </html>}

    
    

    """
    parse_res = {}

    for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        parse_res.update({url:soup})
    return parse_res

        

        
        