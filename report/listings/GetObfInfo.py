
def get_obj_info(clan_member_obj):
    checked_obj = []
    obj_name = []
    obj_counts = []
    for number_i in range(len(clan_member_obj) - 1):
        obj_count = 0
        current_obj = clan_member_obj[number_i + 1]
        if not_in_list(current_obj, checked_obj):
            checked_obj.append(current_obj)
            for number_j in range(len(clan_member_obj)):
                if clan_member_obj[number_j] == current_obj:
                    obj_count += 1
            obj_name.append(current_obj)
            obj_counts.append(obj_count)
    return obj_name, obj_counts

