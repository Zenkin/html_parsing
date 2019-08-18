
def is_title(td_blocks_content):
    if td_blocks_content.find(class_='add') is not None:
        return True
    else:
        return False

