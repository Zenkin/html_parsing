def get_profession_stats(profession_name, profession_count):

    first_profession = []

    first_branch_of_the_second_profession = []
    second_branch_of_the_second_profession = []
    third_branch_of_the_second_profession = []

    percentages_of_first_branch = []
    percentages_of_second_branch = []
    percentages_of_third_branch = []

    first_class = ['Воитель', 'Рыцарь', 'Маг', 'Клерик', 'Светлый Рыцарь', 'Разведчик', 'Светлый Маг', 'Оракул Евы',
                   'Темный Рыцарь', 'Ассасин', 'Темный Маг', 'Оракул Шилен', 'Налетчик', 'Монах', 'Шаман', 'Собиратель',
                   'Ремесленник', 'Солдат', 'Надзиратель']

    for prof in first_class:
        professions, count, first_prof_count = get_second_profession(prof, profession_name, profession_count)
        per = calc_persentage(count)
        first_profession.append(prof)
        prof_length = len(count)
        first_profession.append(' ')
        first_profession.append(' ')

        first_prof_branch = ' '
        second_prof_branch = ' '
        third_prof_branch = ' '

        first_perc_branch = ' '
        second_perc_branch = ' '
        third_perc_branch = ' '

        if prof_length == 3:
            first_prof_branch = professions[0]
            first_perc_branch = per[0]
            second_prof_branch = professions[1]
            second_perc_branch = per[1]
            third_prof_branch = professions[2]
            third_perc_branch = per[2]

        if prof_length == 2:
            first_prof_branch = professions[0]
            first_perc_branch = per[0]
            second_prof_branch = professions[1]
            second_perc_branch = per[1]

        if prof_length == 1:
            first_prof_branch = professions[0]
            first_perc_branch = per[0]

        first_branch_of_the_second_profession.append(first_prof_branch)
        second_branch_of_the_second_profession.append(second_prof_branch)
        third_branch_of_the_second_profession.append(third_prof_branch)

        percentages_of_first_branch.append(first_perc_branch)
        percentages_of_second_branch.append(second_perc_branch)
        percentages_of_third_branch.append(third_perc_branch)

    second_profession = [first_branch_of_the_second_profession,
                         second_branch_of_the_second_profession,
                         third_branch_of_the_second_profession]

    percentages = [percentages_of_first_branch,
                   percentages_of_second_branch,
                   percentages_of_third_branch]

    return first_profession, second_profession, percentages
