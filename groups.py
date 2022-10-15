
# функция подсчета количества пользователей в группе начитная с 0
def group_count(n_customers):
    groups = []
    for n in range(n_customers):
        groups.append(sum(map(int, str(n))))
    from collections import Counter
    count = Counter(groups)
    return count

# функция подсчета количества пользователей в группе начитная с произвольного номера
def group_count_first(n_first_id, n_customers):

    groups = []
    for n in range(n_first_id, n_customers):
        groups.append(sum(map(int, str(n))))
    from collections import Counter
    count = Counter(groups)
    return count


