from src.classes import categories
from typing import List
from src.db_operations import categories_db
from tabulate import tabulate


def show_all_categories():
    results = categories_db.get_all_categories()

    if not results:
        return

    all_categories: List[categories.Category] = []
    all_categories.extend(categories.Category(*result) for result in results)

    flag_max_category_per_line = 0
    table_category = []
    row = []
    for category in all_categories:
        flag_max_category_per_line += 1
        row.append(category.name)
        if flag_max_category_per_line%3 == 0:
            table_category.append(row)
            row=[]
    if row:
        table_category.append(row)

    return table_category

