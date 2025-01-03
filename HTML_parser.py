from html.parser import HTMLParser


class HTML_Parser(HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.img_links = []
        self.base_url = base_url

    def handle_starttag(self, tag, attrs):
        if tag in ('link','script'):
            attrs = dict(attrs)
            if 'rel' in attrs and attrs['rel'] == 'stylesheet':
                link = self._refine(attrs['href'])
                self.img_links.append(link)
            elif 'src' in attrs:
                link = self._refine(attrs['src'])
                self.img_links.append(link)

    def _refine(self, link):
        if not link.startswith(('http://', 'https://')):
            return f'{self.base_url}/{link.lstrip('/')}'
        return link
