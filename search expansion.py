import requests
import urllib
import json
import operator
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession

def get_url(url):
    try:
        session = HTMLSession()
        respose = session.get(url)
        return respose
    except requests.exceptions.RequestException as e:
        print(e)

        def get_result(query):
            response = urllib.parse.quote_plus(query)  # helps in building a query Url
            response = get_url("https://suggestqueries.google.com/complete/search?output=chrome&hl=en&q=" + query)
            results = json.loads(response.text)
            return results

        def order_result(result):
            suggested = []
            for index, value in enumerate(result[1]):
                x = {"term": value, "relevance": result[4]['google:suggestrelevance'][index]}
                suggested.append(x)
            return suggested


def query_expansion(query):
    expanded_term_suffixes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    expanded_term_prefixes = ['who is *', 'what is *', 'where is *', 'when can *', 'why is *',
                              'how to *', 'best', 'cheap', 'worst', 'is', 'what', 'when', 'why',
                              'how', 'who']
    term = []

    for val in expanded_term_prefixes:
        y = val + ' ' + query
        term.append(y)

    for val in expanded_term_suffixes:
        y = query + ' ' + val
        term.append(y)
    return term
