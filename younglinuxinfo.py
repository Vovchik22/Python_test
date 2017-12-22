'''
Дан файл с расписанием занятий на неделю. Помимо названия предмета в нем также указано лекция это
или практическое занятие, или лабораторная работа. В одной строке может быть указаны только один
предмет с информацией о нем. Посчитать, сколько за неделю проходит практических занятий, лекций и
лабораторных работ.
'''

f = open ('lessons.txt', 'r')

lec = pract = lab = 0

for n in f:
    i = n.find('лекц.')
    if i > -1:
        lec += 1
    else:
         i = n.find('практ.')
         if i > -1:
             pract += 1
         else:
             i = n.find('лаб.')
             if i > -1:
                 lab += 1
print(lec)
print(pract)
print(lab)

f.close()