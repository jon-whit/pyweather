import requests
import xml.etree.ElementTree as ET


def fetch_xml(url):
    """
    Fetch a url and parse the document's XML.

    :param url: the URL that the XML is located at.
    :return: the root element of the XML.
    :raises:
        :requests.exceptions.RequestException: Requests could not open the URL.
        :xml.etree.ElementTree.ParseError: xml.etree.ElementTree failed to parse the XML document.
    """
    return ET.parse(requests.get(url, stream=True).raw).getroot()
