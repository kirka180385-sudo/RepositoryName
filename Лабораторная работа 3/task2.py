# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, r = ','):
    clear_first_group = first_group.split(r)
    clear_second_group = second_group.split(r)

    common_participants = list(set(clear_first_group).intersection(clear_second_group))
    common_participants.sort()

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group,'|'))


