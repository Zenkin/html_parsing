def get_clans_statistics(all_members_data):
    clan_member_race = all_members_data[3]
    clan_member_class = all_members_data[2]
    clan_member_lvl = all_members_data[4]
    races, race_counts = get_obj_info(clan_member_race)
    classes, class_counts = get_obj_info(clan_member_class)
    lvls, lvl_counts = get_obj_info(clan_member_lvl)
    races_ratio = get_percentages(races, race_counts)
    classes_ratio = get_percentages(classes, class_counts)
    lvls_ratio = get_percentages(lvls, lvl_counts)
    clan_statistics = [races, race_counts, races_ratio,
                       classes, class_counts,
                       classes_ratio, lvls,
                       lvl_counts, lvls_ratio]
    return clan_statistics
