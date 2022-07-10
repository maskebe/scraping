# Web Scrapping
# https://beautiful-soup-4.readthedocs.io/en/latest/
# https://docs.python.org/3/library/time.html
import re
import time

import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://history.state.gov/'


def dividerLine(n=30):
    print('-' * n)


def fetch(url: str):
    with requests.Session() as session:
        data = session.get(url)
    return data.text

def convertToLink(ref, baseURL):
    """_summary_

    Args:
        a (_type_): _description_

    Returns:
        _type_: _description_
    """
    strTest=str(ref)
    strTest.split(sep='"')
    link = baseURL+strTest.split(sep='"')[1]
    return link


if __name__ == '__main__':
    data = BeautifulSoup(
        fetch('https://history.state.gov/countries/all'),
        features="html.parser"
    )

    regex = re.compile('/countries/\w+')
    lista = data.find_all(href=regex)
    lista = str(lista[2:-1])

   # print(lista.replace(regex, BASE_URL+regex))
