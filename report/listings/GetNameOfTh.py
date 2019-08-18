
def get_name_of_th(html_code):
    th_code = html_code.find('th')
    if th_code.find('a') is not None:
        return str(th_code.find('a').contents[0] + ':')
    else:
        return str(th_code.contents[0])

