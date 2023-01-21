# pymine

This package allows users to provide a list of URLs for webpages of interest and creates a dataframe with Bag of Words representation that can then later be fed into a machine learning model of their choice. Users also have the option to produce a dataframe with just the raw text of their target webpages to apply the text representation of their choice instead.

## Why `pymine`

There are some libraries and packages that can facilitate this job, from scraping text from a URL to returning it to a bag of words (BOW). However, to the extent of our knowledge, there is no sufficiently handy and straightforward package for this purpose. This package is a tailored combination of `BeatifulSoup` and `CountVectorizer`. [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) widely used to pull different sources of data from HTML and XML pages, and [`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) is a well-known package to convert a collection of texts to a matrix of token counts.

### NOTE:

Some websites do not let users collect their data with web scraping tools. Make sure that your target websites do not refuse your request to collect data before applying this package.

## Features

The pymine package includes the following four functions:

-   `create_id()`: Takes a list of webpage urls formatted as strings as an input and returns a list of unique string identifiers for each webpage based on their url. The identifier is composed of the main webpage name followed by a number.
-   `text_from_url()` : Takes a list of urls and using Beautiful Soup extracts the raw text from each and creates a dictionary. The keys contain the original URL and the values contain the raw text output as parsed by Beautiful Soup.
-   `duster()`: Takes a list of urls and uses the above two functions to create a dataframe with the webpage identifiers as a index, the raw url, and the raw text from the webpage with extra line breaks removed.
-   `bow()`: Takes a string text as an input and returns the list of unique words it contains.

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
