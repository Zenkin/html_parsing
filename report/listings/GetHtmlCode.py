
def get_html_code(site_url):
    open_url = urllib.request.urlopen(site_url)
    html_code = open_url.read()
    return html_code

