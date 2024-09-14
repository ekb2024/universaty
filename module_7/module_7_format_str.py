def exempl_format(team1_num, team2_num, score_1, score_2,team1_time ,team2_time ):
     # Использование %:
     print('В команде Мастера кода участников: %s ! ' %team1_num)
     print('Итого сегодня в командах участников: %s и %s !' %(team1_num, team2_num))
     # Использование format()
     print('Команда Волшебники данных решила задач:{} !'.format(score_2))
     print('Волшебники данных решили задачи за {} с !'.format(team1_time))
     # или
     print('Волшебники данных решили задачи за {} {} {}'.format(team1_time,'c','!'))
     # или
     print('Волшебники данных решили задачи за {p1} {p2} {p3}'.format(p1=team1_time, p2='c', p3='!'))
     # Использование f-строк:
     print(f'Команды решили {score_1} и {score_2} задач.')
     tasks_total = score_1 + score_2
     time_avg =  round((team1_time + team2_time) / tasks_total,2)
     print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')
     # или
     print(f'Сегодня было решено {score_1 + score_2} задач, в среднем по {round((team1_time + team2_time)/(score_1 + score_2),2)} секунды на задачу!.')

     if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
         result =  f'‘Победа команды Мастера кода!’'
     elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
       result = f'‘Победа команды Волшебники Данных!’'
     else:
       result = f'‘Ничья!’'
     print(result)

exempl_format(5, 6, 40, 42, 1552.512 , 2153.31451 )

#
#
# if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
#   result = ‘Победа команды Мастера кода!’
# elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
#   result = ‘Победа команды Волшебники Данных!’
# else:
#   result = ‘Ничья!’
#
# team1_num = 5
# team2_num = 6
# score_1 = 40
# score_2 = 42
# team1_time = 1552.512
# team2_time = 2153.31451
#
#
# tasks_total = 82
# time_avg = 45.2
# challenge_result = 'Победа команды Волшебники данных!'

