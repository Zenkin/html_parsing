def get_second_profession(first_prof, all_profession_names, all_profession_counts):
    classes = {'Воитель': ('Копейщик', 'Гладиатор'),
               'Рыцарь': ('Паладин', 'Мститель'),
               'Маг': ('Властитель Огня', 'Некромант', 'Колдун'),
               'Клерик': ('Епископ', 'Проповедник'),
               'Светлый Рыцарь': ('Рыцарь Евы', 'Менестрель'),
               'Разведчик': ('Следопыт', 'Серебряный Рейнджер'),
               'Светлый Маг': ('Певец Заклинаний', 'Последователь Стихий'),
               'Оракул Евы': ['Мудрец Евы'],
               'Темный Рыцарь': ('Рыцарь Шилен', 'Танцор Смерти'),
               'Ассасин': ('Странник Бездны', 'Призрачный Рейнджер'),
               'Темный Маг': ('Заклинатель Ветра', 'Последователь Тьмы'),
               'Оракул Шилен': ['Мудрец Шилен'],
               'Налетчик': ['Разрушитель'],
               'Монах': ['Отшельник'],
               'Шаман': ('Верховный Шаман', 'Вестник Войны'),
               'Собиратель': ['Охотник за Наградой'],
               'Ремесленник': ['Кузнец'],
               'Солдат': ('Берсерк', 'Палач'),
               'Надзиратель': ('Палач', 'Арбалетчик'),
               'Воин Артеи': ['Боец Сайхи'],
               'Маг Артеи': ['Последователь Сайхи']}
    first_prof_count = all_profession_counts[3][all_profession_names[3].index(first_prof)]
    professions = []
    count = []
    second_prof_list = all_profession_names[2]
    second_prof = classes[first_prof]
    for prof in range(len(second_prof)):
        position_in_list = second_prof_list.index(second_prof[prof])
        professions.append(second_prof[prof])
        count.append(all_profession_counts[2][position_in_list])
    return professions, count, first_prof_count
