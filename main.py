from random import randint
# -*- coding: utf-8 -*-
from time import perf_counter

start=perf_counter()

def compress_queue(queue1):
    queue2=[[] for i in range(len(queue1))]
    j=0
    for i in range(len(queue1)):
        if len(queue1[i])>0:
            queue2[j]=queue1[i]
            j+=1
    while len(queue2[0])<sum([len(i) for i in terms_queue])//5:
        for i in range(len(queue2)-1):
            while len(queue2[i+1])>0:
                queue2[i].append(queue2[i+1].pop())


    return queue2


question_width=120

count_right=0
count_wrong=0

blitznumber=int(input('Введите номер блица:'))


with open(f'blitz{blitznumber}.txt',encoding='utf-8') as f:
    terms=[x.strip().split('|') for x in [t for t in f.readlines()]]

terms = [t+[round(len(terms)*0.4)] for t in terms]

terms_queue=[[] for i in range(len(terms))]

terms_queue[0]=[i for i in range(len(terms))]


while len(terms_queue[0])>0:
    rngid = randint(0,len(terms_queue[0])-1)
    id=terms_queue[0][rngid]
    question = terms[id][1]
    question_spl = question.split(' ')
    line = ''
    while len(question_spl)>0:
        line+=' ' + question_spl.pop(0)
        if len(line)>question_width:
            print(line)
            line=''
    if len(line)>0:
        print(line)
    answer = input('> ')
    if answer == terms[id][0]:
        print('Правильно!')
        count_right+=1
        terms[id][2]=round(terms[id][2]*1.6)+1
        terms_queue[0].remove(id)
        if terms[id][2]<len(terms_queue):
            terms_queue[terms[id][2]].append(id)
        else:
            print('Минус один, осталось ', sum([len(i) for i in terms_queue]))
            if sum([len(i) for i in terms_queue]) ==0: break
    else:
        print('Неправильно. Правильный ответ: ', terms[id][0])
        count_wrong+=1
        terms[id][2]=round(terms[id][2]*0.7)+1
        terms_queue[0].remove(id)
        terms_queue[terms[id][2]].append(id)
    terms_queue=compress_queue(terms_queue)
    print('-=-=-=-=-=-=-=-=-=-')

print('-'*100+'\n'+'+'*100+'\n'+'-'*100)
print('Поздравляю, Вы выучили всё!')
print('Всего ответов: ', count_wrong+count_right)
print('Неправильных ответов:', count_wrong)
print('Процент правильных: ', round((count_right/(count_wrong+count_right))*100))
time_spent=round(perf_counter()-start)
print('Вы занимались:', time_spent//60, 'Минут', time_spent%60, 'Секунд.')

input('Enter для выхода')