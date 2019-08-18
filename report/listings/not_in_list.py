
def not_in_list(current_obj, checked_obj):
    for name in checked_obj:
        if name == current_obj:
            return False
    return True

