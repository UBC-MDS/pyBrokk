# pymine

This package allows users to provide a list of URLs for webpages of interest and creates a dataframe with Bag of Words representation that can then later be fed into a machine learning model of their choice. Users also have the option to produce a dataframe with just the raw text of their target webpages to apply the text representation of their choice instead. Finally, users can provide a list of target words or a target class to filter the text that is scraped from their webpages of choice.

## Why `pymine`

There are some libraries and packages that can facilitate this job, from scraping text from a URL to returning it to a bag of words (BOW). However, to the extent of our knowledge, there is no sufficiently handy and straightforward package for this purpose. This package is a tailored combination of `BeatifulSoup` and `CountVectorizer`. [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) widely used to pull different sources of data from HTML and XML pages, and [`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) is a well-known package to convert a collection of texts to a matrix of token counts.

### NOTE:

Some websites do not let users collect their data with web scraping tools. Make sure that your target websites do not refuse your request to collect data before applying this package.

## Features

The pymine package includes the following four functions:

-   `create_id()`: Takes a list of webpage urls formatted as strings as an input and returns a list of unique string identifiers for each webpage based on their url. The identifier is composed of the main webpage name followed by a number.
-   `text_from_url()` : Takes a list of urls and using Beautiful Soup extracts the raw text from each and creates a dataframe. By setting the optional argument identifier it can use the function `create_id()` from this package to add an id column that stores the identifiers for each url.
-   `bow()`: Takes a string text as an input and returns the list of unique words it contains.
-   `count_words()`: Counts the occurrence of a specific list of words on a series of webpages and produces a Pandas dataframe with the results. The user will provide a list of urls to scrape and a list of target words they are interested in.

## Installation

``` bash
$ pip install pymine
```

## Usage

-   TODO

## Contributing

Interested in contributing? Check out the [contributing guidelines](CONTRIBUTING.md) and the [list of contributors](CONTRIBUTORS.md) who have contributed to the development of this project thus far. Please note that this project is released with a [Code of Conduct](CONDUCT.md). By contributing to this project, you agree to abide by these terms.

## License

`pymine` was created by Elena Ganacheva, Mehdi Naji, Mike Guron, Daniel Merigo. It is licensed under the terms of the MIT license.

## Credits

`pymine` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter). `pymine` uses [`beautiful soup`](https://www.crummy.com/software/BeautifulSoup/)
