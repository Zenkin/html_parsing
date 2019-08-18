
def is_in_html_code(html_code, obj):
    flag = False
    for content in html_code.find(class_='values').find_all('a'):
        if content.contents[0] is not None:
            content = content.contents[0]
        if str(content) == str(obj):
            flag = True
    return flag

