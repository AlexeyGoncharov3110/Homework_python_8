# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [23,14,23,'fail','text',True,False,12,23,12,454,'fail']
dublicate = []
for i in my_list:
    if my_list.count(i)>1:
        dublicate.append(i) 

print(set(dublicate))

def find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

lst = [23,14,23,'fail','text',True,False,12,23,12,454,'fail']
print(find_duplicates(lst))