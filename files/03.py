from pyexpat import features
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://history.state.gov/'
URL = 'https://history.state.gov/countries/all'
def fetch(url):
    with requests.Session() as session:
        data = session.get(url)
        return data.text

data = BeautifulSoup(
    fetch(URL),
    features = "html.parser"
)

#pretify data for display
#pretty = data.prettify()

if __name__ == '__main__':
    #find h2 tag in the dom
    varh2 = data.find("h2")

    #find all h2 tag in the dom
    varAllh2 = data.find_all('h2')

    #get the name of the element
    name = varh2.name

    #get all h3 tags
    varh3 = data.find_all("h3")

    print(varh2)
    print('\n')
    print(varAllh2)
    print('\n')
    print(name)
    print('\n')
    print(varh3)


