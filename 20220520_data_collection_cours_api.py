
import requests
import json

def divider(n=20):
    return '-' * n


if __name__ == '__main__':

    page = requests.get('https://api.datamuse.com/words?rel_rhy=funny')
    print(divider())
    print(type(page))
    print(divider)
    print('\n')