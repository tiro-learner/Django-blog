from django.template import Library
from re import sub
from sys import stderr
from traceback import print_exc
from html.parser import  HTMLParser

register = Library()

class _DeHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__text = []

    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0:
            text = sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n\n')
        elif tag == 'br':
            self.__text.append('\n')

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.__text.append('\n\n')

    def text(self):
        return ''.join(self.__text).strip()


def dehtml_parse(html_text):
    try:
        parser = _DeHTMLParser()
        parser.feed(html_text)
        parser.close()
        return parser.text()

    except:
        print_exc(file=stderr)
        return html_text


register.filter("dehtml", dehtml_parse)