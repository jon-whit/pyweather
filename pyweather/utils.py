import requests
import xml.etree.ElementTree as ET
from urllib.parse import quote


def fetch_xml(url):
    """
    Fetch a url and parse the document's XML.

    :param url: the URL that the XML is located at.
    :return: the root element of the XML.
    """

    return ET.fromstring(requests.get(url).content)

def fetch_woeid(location):
    """
    Fetch a location's corresponding WOEID.

    :param location: (string) a location (e.g. 23454 or Salt Lake City, United States)
    :return: a string containing the location's corresponding WOEID or None if the WOEID could not be found.
    """

    woeid_query = ("http://locdrop.query.yahoo.com/v1/public/yql?"
                   "q=select%20woeid%20from%20locdrop.placefinder%20"
                   "where%20text='{0}'")
    url = woeid_query.format(quote(location))

    rss = fetch_xml(url)

    try:
        woeid = rss.find("results/Result/woeid").text
    except AttributeError:
        return None

    return woeid
