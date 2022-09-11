def filter_query(param, data):
    """Функция фильтрации данных."""
    return list(filter(lambda x: param in x, data))


def map_query(param, data):
    """Функция получает номер колонки и выводит списком данные этой колонки."""
    col_number = int(param)
    return list(map(lambda x: x.split(' ')[col_number], data))


def unique_query(data, *args, **kwargs):
    """Функция создает список из уникальных позиций."""
    return list(set(data))


def sort_query(param, data):
    """ Функция сортировки данных."""
    reverse = False if param == 'asc' else True
    return sorted(data, reverse=reverse)


def limit_query(param, data):
    """Функция создает список позиций в заданном количестве."""
    limit = int(param)
    return list(data)[:limit]
