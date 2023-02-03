import time
TIME1 = time.perf_counter()

import re
import pandas as pd
import numpy as np
from urllib.parse import unquote, urlparse
import pymorphy2
from pymorphy2 import tokenizers
morph = pymorphy2.MorphAnalyzer()

"""считываем бд, директорию поменять"""
df = pd.read_csv('C:\\Users\\Lenovo\\Desktop\\fl\\1\\harvest_copy.csv')
#df = df.head(10000)
#df.to_csv('C:\\Users\\Lenovo\\Desktop\\fl\\1\\harvest_copy.csv')

###фильтруем бд от лишних строк
dff = df[df.link_type != 'link_type']

###массив с типами урл
#lt = dff.link_type.unique()
#print(lt)

###самые частые слова в описании урл с категорией "контакт"
def function_contact_ttl():
    ###фильтруем для типа "контакт"
    dff_contact = dff[dff.link_type == 'contact']
    ###уникальные описания для категории "контакт"
    ttl = dff_contact.title.unique()
    
    ###разбиваем строки на слова
    ttl1 = []
    for i in range (len(ttl)-1):
        token_ttl = tokenizers.simple_word_tokenize(str(ttl[i]))
        ttl1.append(token_ttl)

    ###фильтруем слова
    ###перевод в нижний регистр
    ttl2 = []
    for i in ttl1:
        for j in i:
            ttl2.append(j.lower())

    ###удаление небуквенных символов и слов короче 5 символов
    ttl3=[]
    for i in ttl2:
        i = re.sub("</?.*?>"," <> ", i)
        i = re.sub("(\\d|\\W)+", " " , i)
        for j in i:
            for k in i:
                if j in 'qwertyuiopasdfghjklzxcvbnm -' and k in "йцукенгшщзхъфывапролджэячсмитьбю":
                    i = i.replace(j, '')
        if len(i)>4:
            ttl3.append(i)

    ###перевод слова в начальную форму
    ttl4 = []
    for i in ttl3:
        ttl4.append(morph.parse(i)[0].normal_form)

    ###создаем словарь, ключ - слово, значение - количество (установлено больше 10, можно изменить)
    counter_ttl = {}
    for i in ttl4:
        counter_ttl[i] = counter_ttl.get(i, 0) + 1
    doubles_ttl = {element: count for element, count in counter_ttl.items() if count > 0}
    ttl = dict(sorted(doubles_ttl.items(), reverse = True, key=lambda x: x[1]))

    """запись в файл, директорию поменять"""
    with open('C:\\Users\\Lenovo\\Desktop\\fl\\1\\contact_title.txt','w',encoding='utf-8') as out:
        for key,val in ttl.items():
            out.write('{}:{}\n'.format(key,val))

    return 0

###самые частые слова в урл с категорией "контакт"
def function_contact_url():
    ###фильтруем для типа "контакт"
    dff_contact = dff[dff.link_type == 'contact']
    ###уникальные урл для категории "контакт"
    url_name = dff_contact.url.unique()
    ###черный список слов
    url_bl = ['html', 'php', 'asp', 'aspx', 'xhtml', 'index']
    url_name1 = []

    ###разбиваем строки на слова
    for i in url_name:
        tokens = re.split('\/|\%20|-|_| |\.', unquote(urlparse(i).path))
        filtered_tokens = list(
            filter(
                lambda x: x != '' and x not in url_bl and len(x) > 3 and not x.isnumeric(), tokens
            )
        )
        for j in list(set([_token.lower() for _token in filtered_tokens])):
            url_name1.append(j)

    ###создаем словарь, ключ - слово, значение - количество
    counter_url = {}
    for i in url_name1:
        counter_url[i] = counter_url.get(i, 0) + 1
    doubles_url = {element: count for element, count in counter_url.items() if count > 0}
    url_name = dict(sorted(doubles_url.items(), reverse = True, key=lambda x: x[1]))


    """запись в файл, директорию поменять"""
    with open('C:\\Users\\Lenovo\\Desktop\\fl\\1\\contact_url.txt','w',encoding='utf-8') as out:
        for key,val in url_name.items():
            out.write('{}:{}\n'.format(key,val))

    return 0



###самые частые слова в описании урл с категорией "реквизит"
def function_requisite_ttl():
    ###фильтруем для типа "реквизит"
    dff_requisite = dff[dff.link_type == 'requisite']
    ###уникальные описания для категории "реквизит"
    ttl = dff_requisite.title.unique()
    
    ###разбиваем строки на слова
    ttl1 = []
    for i in range (len(ttl)-1):
        token_ttl = tokenizers.simple_word_tokenize(str(ttl[i]))
        ttl1.append(token_ttl)

    ###фильтруем слова
    ###перевод в нижний регистр
    ttl2 = []
    for i in ttl1:
        for j in i:
            ttl2.append(j.lower())

    ###удаление небуквенных символов и слов короче 5 символов
    ttl3=[]
    for i in ttl2:
        i = re.sub("</?.*?>"," <> ", i)
        i = re.sub("(\\d|\\W)+", " " , i)
        for j in i:
            for k in i:
                if j in 'qwertyuiopasdfghjklzxcvbnm -' and k in "йцукенгшщзхъфывапролджэячсмитьбю":
                    i = i.replace(j, '')
        if len(i)>4:
            ttl3.append(i)

    ###перевод слова в начальную форму
    ttl4 = []
    for i in ttl3:
        ttl4.append(morph.parse(i)[0].normal_form)

    ###создаем словарь, ключ - слово, значение - количество (установлено больше 0, можно изменить)
    counter_ttl = {}
    for i in ttl4:
        counter_ttl[i] = counter_ttl.get(i, 0) + 1
    doubles_ttl = {element: count for element, count in counter_ttl.items() if count > 0}
    ttl = dict(sorted(doubles_ttl.items(), reverse = True, key=lambda x: x[1]))

    """запись в файл, директорию поменять"""
    with open('C:\\Users\\Lenovo\\Desktop\\fl\\1\\requisite_title.txt','w',encoding='utf-8') as out:
        for key,val in ttl.items():
            out.write('{}:{}\n'.format(key,val))

    return 0

###самые частые слова в урл с категорией "реквизит"
def function_requisite_url():
    ###фильтруем для типа "реквизит"
    dff_requisite = dff[dff.link_type == 'requisite']
    ###уникальные урл для категории "реквизит"
    url_name = dff_requisite.url.unique()
    ###черный список слов
    url_bl = ['html', 'php', 'asp', 'aspx', 'xhtml', 'index']
    url_name1 = []

    ###разбиваем строки на слова
    for i in url_name:
        tokens = re.split('\/|\%20|-|_| |\.', unquote(urlparse(i).path))
        filtered_tokens = list(
            filter(
                lambda x: x != '' and x not in url_bl and len(x) > 3 and not x.isnumeric(), tokens
            )
        )
        for j in list(set([_token.lower() for _token in filtered_tokens])):
            url_name1.append(j)

    ###создаем словарь, ключ - слово, значение - количество (установлено больше 0, можно изменить)
    counter_url = {}
    for i in url_name1:
        counter_url[i] = counter_url.get(i, 0) + 1
    doubles_url = {element: count for element, count in counter_url.items() if count > 0}
    url_name = dict(sorted(doubles_url.items(), reverse = True, key=lambda x: x[1]))


    """запись в файл, директорию поменять"""
    with open('C:\\Users\\Lenovo\\Desktop\\fl\\1\\requisite_url.txt','w',encoding='utf-8') as out:
        for key,val in url_name.items():
            out.write('{}:{}\n'.format(key,val))

    return 0



###самые частые слова в описании урл с категорией "about"
def function_about_ttl():
    ###фильтруем для типа "about"
    dff_about = dff[dff.link_type == 'about']
    ###уникальные описания для категории "about"
    ttl = dff_about.title.unique()
    
    ###разбиваем строки на слова
    ttl1 = []
    for i in range (len(ttl)-1):
        token_ttl = tokenizers.simple_word_tokenize(str(ttl[i]))
        ttl1.append(token_ttl)

    ###фильтруем слова
    ###перевод в нижний регистр
    ttl2 = []
    for i in ttl1:
        for j in i:
            ttl2.append(j.lower())

    ###удаление небуквенных символов и слов короче 5 символов
    ttl3=[]
    for i in ttl2:
        i = re.sub("</?.*?>"," <> ", i)
        i = re.sub("(\\d|\\W)+", " " , i)
        for j in i:
            for k in i:
                if j in 'qwertyuiopasdfghjklzxcvbnm -' and k in "йцукенгшщзхъфывапролджэячсмитьбю":
                    i = i.replace(j, '')
        if len(i)>4:
            ttl3.append(i)

    ###перевод слова в начальную форму
    ttl4 = []
    for i in ttl3:
        ttl4.append(morph.parse(i)[0].normal_form)

    ###создаем словарь, ключ - слово, значение - количество (установлено больше 0, можно изменить)
    counter_ttl = {}
    for i in ttl4:
        counter_ttl[i] = counter_ttl.get(i, 0) + 1
    doubles_ttl = {element: count for element, count in counter_ttl.items() if count > 0}
    ttl = dict(sorted(doubles_ttl.items(), reverse = True, key=lambda x: x[1]))

    """запись в файл, директорию поменять"""
    with open('C:\\Users\\Lenovo\\Desktop\\fl\\1\\about_title.txt','w',encoding='utf-8') as out:
        for key,val in ttl.items():
                out.write('{}:{}\n'.format(key,val))

    return 0

###самые частые слова в урл с категорией "about"
def function_about_url():
    ###фильтруем для типа "about"
    dff_about = dff[dff.link_type == 'about']
    ###уникальные урл для категории "about"
    url_name = dff_about.url.unique()
    ###черный список слов
    url_bl = ['html', 'php', 'asp', 'aspx', 'xhtml', 'index']
    url_name1 = []

    ###разбиваем строки на слова
    for i in url_name:
        tokens = re.split('\/|\%20|-|_| |\.', unquote(urlparse(i).path))
        filtered_tokens = list(
            filter(
                lambda x: x != '' and x not in url_bl and len(x) > 3 and not x.isnumeric(), tokens
            )
        )
        for j in list(set([_token.lower() for _token in filtered_tokens])):
            url_name1.append(j)

    ###создаем словарь, ключ - слово, значение - количество (установлено больше 0, можно изменить)
    counter_url = {}
    for i in url_name1:
        counter_url[i] = counter_url.get(i, 0) + 1
    doubles_url = {element: count for element, count in counter_url.items() if count > 0}
    url_name = dict(sorted(doubles_url.items(), reverse = True, key=lambda x: x[1]))


    """запись в файл, директорию поменять"""
    with open('C:\\Users\\Lenovo\\Desktop\\fl\\1\\about_url.txt','w',encoding='utf-8') as out:
        for key,val in url_name.items():
            out.write('{}:{}\n'.format(key,val))

    return 0



###самые частые слова в описании урл с категорией "оплата"
def function_payment_ttl():
    ###фильтруем для типа "оплата"
    dff_payment = dff[dff.link_type == 'payment']
    ###уникальные описания для категории "оплата"
    ttl = dff_payment.title.unique()
    
    ###разбиваем строки на слова
    ttl1 = []
    for i in range (len(ttl)-1):
        token_ttl = tokenizers.simple_word_tokenize(str(ttl[i]))
        ttl1.append(token_ttl)

    ###фильтруем слова
    ###перевод в нижний регистр
    ttl2 = []
    for i in ttl1:
        for j in i:
            ttl2.append(j.lower())

    ###удаление небуквенных символов и слов короче 5 символов
    ttl3=[]
    for i in ttl2:
        i = re.sub("</?.*?>"," <> ", i)
        i = re.sub("(\\d|\\W)+", " " , i)
        for j in i:
            for k in i:
                if j in 'qwertyuiopasdfghjklzxcvbnm -' and k in "йцукенгшщзхъфывапролджэячсмитьбю":
                    i = i.replace(j, '')
        if len(i)>4:
            ttl3.append(i)

    ###перевод слова в начальную форму
    ttl4 = []
    for i in ttl3:
        ttl4.append(morph.parse(i)[0].normal_form)

    ###создаем словарь, ключ - слово, значение - количество (установлено больше 0, можно изменить)
    counter_ttl = {}
    for i in ttl4:
        counter_ttl[i] = counter_ttl.get(i, 0) + 1
    doubles_ttl = {element: count for element, count in counter_ttl.items() if count > 0}
    ttl = dict(sorted(doubles_ttl.items(), reverse = True, key=lambda x: x[1]))

    """запись в файл, директорию поменять"""
    with open('C:\\Users\\Lenovo\\Desktop\\fl\\1\\payment_title.txt','w',encoding='utf-8') as out:
        for key,val in ttl.items():
            out.write('{}:{}\n'.format(key,val))

    return 0

###самые частые слова в урл с категорией "оплата"
def function_payment_url():
    ###фильтруем для типа "оплата"
    dff_payment = dff[dff.link_type == 'payment']
    ###уникальные урл для категории "оплата"
    url_name = dff_payment.url.unique()
    ###черный список слов
    url_bl = ['html', 'php', 'asp', 'aspx', 'xhtml', 'index']
    url_name1 = []

    ###разбиваем строки на слова
    for i in url_name:
        tokens = re.split('\/|\%20|-|_| |\.', unquote(urlparse(i).path))
        filtered_tokens = list(
            filter(
                lambda x: x != '' and x not in url_bl and len(x) > 3 and not x.isnumeric(), tokens
            )
        )
        for j in list(set([_token.lower() for _token in filtered_tokens])):
            url_name1.append(j)

    ###создаем словарь, ключ - слово, значение - количество (установлено больше 0, можно изменить)
    counter_url = {}
    for i in url_name1:
        counter_url[i] = counter_url.get(i, 0) + 1
    doubles_url = {element: count for element, count in counter_url.items() if count > 0}
    url_name = dict(sorted(doubles_url.items(), reverse = True, key=lambda x: x[1]))


    """запись в файл, директорию поменять"""
    with open('C:\\Users\\Lenovo\\Desktop\\fl\\1\\payment_url.txt','w',encoding='utf-8') as out:
        for key,val in url_name.items():
            out.write('{}:{}\n'.format(key,val))

    return 0



###самые частые слова в описании урл с категорией "доставка"
def function_delivery_ttl():
    ###фильтруем для типа "доставка"
    dff_delivery = dff[dff.link_type == 'delivery']
    ###уникальные описания для категории "доставка"
    ttl = dff_delivery.title.unique()
    
    ###разбиваем строки на слова
    ttl1 = []
    for i in range (len(ttl)-1):
        token_ttl = tokenizers.simple_word_tokenize(str(ttl[i]))
        ttl1.append(token_ttl)

    ###фильтруем слова
    ###перевод в нижний регистр
    ttl2 = []
    for i in ttl1:
        for j in i:
            ttl2.append(j.lower())

    ###удаление небуквенных символов и слов короче 5 символов
    ttl3=[]
    for i in ttl2:
        i = re.sub("</?.*?>"," <> ", i)
        i = re.sub("(\\d|\\W)+", " " , i)
        for j in i:
            for k in i:
                if j in 'qwertyuiopasdfghjklzxcvbnm -' and k in "йцукенгшщзхъфывапролджэячсмитьбю":
                    i = i.replace(j, '')
        if len(i)>4:
            ttl3.append(i)

    ###перевод слова в начальную форму
    ttl4 = []
    for i in ttl3:
        ttl4.append(morph.parse(i)[0].normal_form)

    ###создаем словарь, ключ - слово, значение - количество (установлено больше 0, можно изменить)
    counter_ttl = {}
    for i in ttl4:
        counter_ttl[i] = counter_ttl.get(i, 0) + 1
    doubles_ttl = {element: count for element, count in counter_ttl.items() if count > 0}
    ttl = dict(sorted(doubles_ttl.items(), reverse = True, key=lambda x: x[1]))

    """запись в файл, директорию поменять"""
    with open('C:\\Users\\Lenovo\\Desktop\\fl\\1\\delivery_title.txt','w',encoding='utf-8') as out:
        for key,val in ttl.items():
            out.write('{}:{}\n'.format(key,val))

    return 0

###самые частые слова в урл с категорией "доставка"
def function_delivery_url():
    ###фильтруем для типа "доставка"
    dff_delivery = dff[dff.link_type == 'delivery']
    ###уникальные урл для категории "доставка"
    url_name = dff_delivery.url.unique()
    ###черный список слов
    url_bl = ['html', 'php', 'asp', 'aspx', 'xhtml', 'index']
    url_name1 = []

    ###разбиваем строки на слова
    for i in url_name:
        tokens = re.split('\/|\%20|-|_| |\.', unquote(urlparse(i).path))
        filtered_tokens = list(
            filter(
                lambda x: x != '' and x not in url_bl and len(x) > 3 and not x.isnumeric(), tokens
            )
        )
        for j in list(set([_token.lower() for _token in filtered_tokens])):
            url_name1.append(j)

    ###создаем словарь, ключ - слово, значение - количество (установлено больше 0, можно изменить)
    counter_url = {}
    for i in url_name1:
        counter_url[i] = counter_url.get(i, 0) + 1
    doubles_url = {element: count for element, count in counter_url.items() if count > 0}
    url_name = dict(sorted(doubles_url.items(), reverse = True, key=lambda x: x[1]))


    """запись в файл, директорию поменять"""
    with open('C:\\Users\\Lenovo\\Desktop\\fl\\1\\delivery_url.txt','w',encoding='utf-8') as out:
        for key,val in url_name.items():
            out.write('{}:{}\n'.format(key,val))

    return 0



###самые частые слова в описании урл с категорией "другое"
def function_other_ttl():
    ###фильтруем для типа "другое"
    dff_other = dff[dff.link_type == 'other']
    ###уникальные описания для категории "другое"
    ttl = dff_other.title.unique()
    
    ###разбиваем строки на слова
    ttl1 = []
    for i in range (len(ttl)-1):
        token_ttl = tokenizers.simple_word_tokenize(str(ttl[i]))
        ttl1.append(token_ttl)

    ###фильтруем слова
    ###перевод в нижний регистр
    ttl2 = []
    for i in ttl1:
        for j in i:
            ttl2.append(j.lower())

    ###удаление небуквенных символов и слов короче 5 символов
    ttl3=[]
    for i in ttl2:
        i = re.sub("</?.*?>"," <> ", i)
        i = re.sub("(\\d|\\W)+", " " , i)
        for j in i:
            for k in i:
                if j in 'qwertyuiopasdfghjklzxcvbnm -' and k in "йцукенгшщзхъфывапролджэячсмитьбю":
                    i = i.replace(j, '')
        if len(i)>4:
            ttl3.append(i)

    ###перевод слова в начальную форму
    ttl4 = []
    for i in ttl3:
        ttl4.append(morph.parse(i)[0].normal_form)

    ###создаем словарь, ключ - слово, значение - количество (установлено больше 0, можно изменить)
    counter_ttl = {}
    for i in ttl4:
        counter_ttl[i] = counter_ttl.get(i, 0) + 1
    doubles_ttl = {element: count for element, count in counter_ttl.items() if count > 0}
    ttl = dict(sorted(doubles_ttl.items(), reverse = True, key=lambda x: x[1]))

    """запись в файл, директорию поменять"""
    with open('C:\\Users\\Lenovo\\Desktop\\fl\\1\\other_title.txt','w',encoding='utf-8') as out:
        for key,val in ttl.items():
            out.write('{}:{}\n'.format(key,val))

    return 0

###самые частые слова в урл с категорией "другое"
def function_other_url():
    ###фильтруем для типа "другое"
    dff_other = dff[dff.link_type == 'other']
    ###уникальные урл для категории "другое"
    url_name = dff_other.url.unique()
    ###черный список слов
    url_bl = ['html', 'php', 'asp', 'aspx', 'xhtml', 'index']
    url_name1 = []

    ###разбиваем строки на слова
    for i in url_name:
        tokens = re.split('\/|\%20|-|_| |\.', unquote(urlparse(i).path))
        filtered_tokens = list(
            filter(
                lambda x: x != '' and x not in url_bl and len(x) > 3 and not x.isnumeric(), tokens
            )
        )
        for j in list(set([_token.lower() for _token in filtered_tokens])):
            url_name1.append(j)

    ###создаем словарь, ключ - слово, значение - количество (установлено больше 0, можно изменить)
    counter_url = {}
    for i in url_name1:
        counter_url[i] = counter_url.get(i, 0) + 1
    doubles_url = {element: count for element, count in counter_url.items() if count > 0}
    url_name = dict(sorted(doubles_url.items(), reverse = True, key=lambda x: x[1]))


    """запись в файл, директорию поменять"""
    with open('C:\\Users\\Lenovo\\Desktop\\fl\\1\\other_url.txt','w',encoding='utf-8') as out:
        for key,val in url_name.items():
            out.write('{}:{}\n'.format(key,val))

    return 0



###повторная сортировка сайтов с категорией "другое"
def function_second_sort_other():
    ###создаем пустой файл для записи строк
    with open('C:\\Users\\Lenovo\\Desktop\\fl\\1\\outfile1.csv', 'w'):
        pass

    ###фильтруем для типа "другое"
    dff_other = dff[dff.link_type == 'other']

    ###черный список слов
    url_bl = ['html', 'php', 'asp', 'aspx', 'xhtml', 'index']

    ###ключевые слова и черные списки слов для всех категорий
    url_cont_ab_req = ['contacts', 'kontakty', 'contact', 'kontakti', 'kontaktnye', 'kontaktyi', 'kontakt', 
        'feedback', 'контакты', 'kontaktnaya', 'kontaktnoy', 'kontaktnoj', 'kontaktov', 'requisites', 
        'rekvizity', 'rekviziti', 'rekvizit', 'rekvizityi', 'requisite', 'реквизиты', 'bank', 'bankovskie', 
        'about', 'info', 'information']
    ttl_cont_ab_req = ['контакт', 'контактный', 'contact', 'реквизит', 'банковский', 'банк', 'сбербанк', 
        'информация', 'about', 'информационный', 'адрес']
    url_cont_ab_req_bl = ['prazdnik', 'prazdnichnyi', 'zoo', 'zoopark', 'linzy', 'linzi', 'lens', 'lenses', 
        'линзы', 'праздник', 'аниматор', 'аниматоры', 'animator', 'animatory', 'animators', 'svarka', 'welding',
        'svarochnoe', 'foto', 'fotography', 'fotografiya', 'fotosessiya', 'fotosession', 'фото', 'фотосессия']
    ttl_cont_ab_req_bl = ['праздник', 'праздничный', 'зоопарк', 'животное', 'линза', 'линзы', 'аниматор', 
        'аниматоры', 'сварка', 'сварочное', 'фото', 'фотография', 'фотосессия']
    

    url_del_pay = ['payment', 'oplata', 'payments', 'оплата', 'dostavka', 'delivery', 
        'shipping', 'доставка', 'marshrut', 'dostavke']
    ttl_del_pay = ['оплата', 'предоплата', 'доставка', 'самовывоз', 'курьер', 'доставить']
    url_del_pay_bl = ['sale', 'skidka', 'skidki', 'catalog']
    ttl_del_pay_bl = ['скидка', 'акция']


    url_news = ['news', 'articles', 'novosti', 'article', 'review', 'blog', 'otzyvy', 'otzyv', 'politika', 
        'help', 'content', 'wishlist', 'vozvrat', 'garantiya', 'feedback', 'vacancy', 'vacansiya', 'vakansiya']
    ttl_news = ['новость', 'украина', 'россия', 'политика', 'описание', 'гарантия', 'инструкция', 'сертификат', 
        'помощь', 'вакансия', 'возврат']
    url_news_bl = ['usluga', 'uslugi', 'sale', 'skidka', 'skidki', 'catalog', 'market']
    ttl_news_bl = ['услуга', 'скидка', 'акция']


    url_product = ['product', 'products', 'tovary', 'katalog', 'produkty', 
        'catalog', 'market', 'category', 'aksessuary', 'categories', 'zapchasti', 'odezhda', 
        'dveri', 'sistemy', 'sistem', 'materialy', 'brands', 'svetilniki', 'goods', 'good', 'catalogue', 
        'compare', 'produktsiya', 'kosmetika', 'sale', 'komplekty', 'furnitura', 'accessories', 'iphone',
        'rasprodazha', 'bytovaya', 'kirpich', 'akkumulyatory', 'market', 'xiaomi', 'apple', 'samsung',
        'usluga', 'uslugi', 'skidka', 'skidki']
    ttl_product = ['apple', 'смартфон', 'xiaomi', 'товар', 'зоотовар', 'канцтовары', 
        'электротовар', 'автотовар', 'хозтовары', 'iphone', 'каталог', 'оптом', 'цена', 'оборудование',
        'мебель', 'продажа', 'система', 'аксессуар', 'одежда', 'услуга', 'скидка', 'техника', 'розница',
        'установка', 'инструмент', 'акция', 'продукция', 'категория']
    url_product_bl = []
    ttl_product_bl = []
    

    url_login = ['auth', 'registration', 'register', 'registrate', 'signup']
    ttl_login = ['регистрация', 'пароль', 'логин', 'имя', 'зарегистрировать']
    url_login_bl = []
    ttl_login_bl = []
    

    url_cart = ['cart', 'basket', 'order', 'zakaz']
    ttl_cart = ['корзина', 'корзинка']
    url_cart_bl = ['bank', 'bankovskaya', 'cartoon', 'multik', 'multiki', 'multfilf', 'multserial']
    ttl_cart_bl = ['банк', 'банковская', 'мультик', 'мультфильм', 'мультсериал', 'мульт']
    

    #!!! Объединяем все группы урлов в один словарь
    #!!! словари наше всё, главное понять как и что завернуть (что сделаеть ключом, а что - значением)
    #!!! на пандас может быть тоже можно такое провернуть, но я просто больше работаю с голым пайтоном
    ###отдельные группы для урл, описания и черных списков для урл и описания
    url_groups = {
        'contact, requisite, about': url_cont_ab_req,
        'payment, delivery': url_del_pay,
        'news': url_news, 
        'product': url_product, 
        'login': url_login, 
        'cart': url_cart
    }
    url_groups_bl = {
        'contact, requisite, about': url_cont_ab_req_bl, 
        'payment, delivery': url_del_pay_bl, 
        'news': url_news_bl, 
        'product': url_product_bl, 
        'login': url_login_bl, 
        'cart': url_cart_bl
    }

    title_groups = {
        'contact, requisite, about': ttl_cont_ab_req, 
        'payment, delivery': ttl_del_pay, 
        'news': ttl_news, 
        'product': ttl_product, 
        'login': ttl_login, 
        'cart': ttl_cart
    }
    title_groups_bl = {
        'contact, requisite, about': ttl_cont_ab_req_bl, 
        'payment, delivery': ttl_del_pay_bl, 
        'news': ttl_news_bl, 
        'product': ttl_product_bl, 
        'login': ttl_login_bl, 
        'cart': ttl_cart_bl
    }
    

    ###разбиваем строки на слова
    dff_other = dff_other.reindex(dff_other.columns.to_list() + ['link_type2'], axis=1)
    print(len(dff_other))
    quant_str = 1
    ###таймер для 1000 строк
    count = 0
    start = int(time.time())
    dff_other1 = dff_other.head(0)
    dff_other1.to_csv('C:\\Users\\Lenovo\\Desktop\\fl\\1\\outfile1.csv', mode = 'a', index = False)
    for strings in range (1, len(dff_other), quant_str):
        count += 1
        if count % 1000 == 0:
                now = int(time.time())
                print(count, now - start)
                start = int(time.time())
        ###саздаем дф с одной строкой, тк построчно работает быстрее
        dff_other_cycle = pd.concat([dff_other.head(0), dff_other[strings:strings+quant_str]], ignore_index = True)
        
        ###счетчик слов в урл и описании, для каждой строки создается новый
        categories_counter = {
                'contact, requisite, about': 0, 
                'payment, delivery': 0, 
                'news': 0, 
                'product': 0, 
                'login': 0, 
                'cart': 0
            }
        
        ###разбиваем урл на слова
        for adress in dff_other_cycle.url:
            tokens = re.split('\/|\%20|-|_| |\.', unquote(urlparse(adress).path))
            filtered_tokens = list(
                filter(
                    lambda x: x != '' and x not in url_bl and len(x) > 3 and not x.isnumeric(), tokens
                )
            )
        
        ###разбиваем описание на слова, приводим к нижнему регистру и в начальную форму,
        ###удаляем все лишние символы
        ttl1=[]
        for a in dff_other_cycle.title:
            token_ttl = tokenizers.simple_word_tokenize(str(a))
            ttl1.append(token_ttl)
        ttl2 = []
        for a in ttl1:
            for j in a:
                ttl2.append(j.lower())
        ttl3=[]
        for a in ttl2:
            a = re.sub("</?.*?>"," <> ", a)
            a = re.sub("(\\d|\\W)+", " " , a)
            for j in a:
                for k in a:
                    if j in 'qwertyuiopasdfghjklzxcvbnm -' and k in "йцукенгшщзхъфывапролджэячсмитьбю":
                        a = a.replace(j, '')
            if len(a)>4:
                ttl3.append(a)
        ttl4 = []
        for a in ttl3:
            ttl4.append(morph.parse(a)[0].normal_form)

        #!!! Объявляем словарь с счетчиками. Так код будет лакончинее, а подсчеты такие же простые
        #!!! для простоты ключи называем также как и в словаре с группами урлов выше
        
        for j in list(set([_token.lower() for _token in filtered_tokens])):
            #!!! Вместо кучи ветвлений делаем сложную конструкцию из одного цикла
            #!!! это тоже получается довольно долго за счет вложенного цикла, но зато код понятнее
            #!!! и ещё совет по поводу j и других названий переменных. 
            #!!! лучше называть более явно переменные, чтобы сохранялся контекст и читаемость, как в цикле ниже
            #!!! итерируем по ключу (названию группы) и значения (список с паттернами урлов) словаря 
            for _url_group_name, _url_group_list in url_groups.items():
                #!!! проверяем, что паттерн, который мы проверяем, находится в списке паттернов
                if j in _url_group_list:
                    #!!! и если так, то инкрементируем счетчик в словаре счетчика
                    categories_counter[_url_group_name] += 1

        ###аналогично предыдущему, но для черного списка
        ###тк это чс, то счетчик в минус на более весомое значение
        ###чтобы включение этого слова точно показывало, что урл к категории не имеет отношения
        for j in list(set([_token.lower() for _token in filtered_tokens])):
            for _url_group_name_bl, _url_group_list_bl in url_groups_bl.items():
                if j in _url_group_list_bl:
                    categories_counter[_url_group_name_bl] -= 5
        
        ###аналогично предыдущему
        for j in ttl4:
            for _title_group_name, _title_group_list in title_groups.items():
                if j in _title_group_list:
                    categories_counter[_title_group_name] += 1
        
        ###аналогично предыдущему, но для черного списка
        for j in ttl4:
            for _title_group_name_bl, _title_group_list_bl in title_groups_bl.items():
                if j in _title_group_list_bl:
                    categories_counter[_title_group_name_bl] -= 5

        #!!! после этого нам необходимо только найти максимальное значение из словаря со счетчиками
        #!!! делается это всё в одну строчку
        #!!! тут лучше почитать официальну доку  - https://docs.python.org/3/library/functions.html#max
        #!!! в переменной max_category_name будет храниться название категории (url_contact, url_news) с максимальным счетчиком 
        max_category_name = max(categories_counter, key=categories_counter.get)
        ###этот список необходим для оценки ошибочного присвоения (2-3 категории с одинаковым счетчиком)
        sorted_categories_counter = list(sorted(categories_counter.items(), key = lambda item: item[1], reverse = True))
        ###присвоение категории
        if sorted_categories_counter[0][1] == sorted_categories_counter[1][1] == sorted_categories_counter[2][1] != 0:
            dff_other_cycle.loc[dff_other_cycle['url'] == adress, 'link_type2'] = '3 categorys'
        elif sorted_categories_counter[0][1] == sorted_categories_counter[1][1] != 0:
            dff_other_cycle.loc[dff_other_cycle['url'] == adress, 'link_type2'] = '2 categorys'
        elif sorted_categories_counter[0][1] != 0:
            dff_other_cycle.loc[dff_other_cycle['url'] == adress, 'link_type2'] = max_category_name
        else:
            dff_other_cycle.loc[dff_other_cycle['url'] == adress, 'link_type2'] = 'other'
        
        ###запись в файл построчно
        dff_other_cycle.to_csv('C:\\Users\\Lenovo\\Desktop\\fl\\1\\outfile1.csv', mode = 'a', index = False, header = False)
    
    return 0
    
###оценка результатов работы функции повторной сортировки
def res_ev():
    df = pd.read_csv('C:\\Users\\Lenovo\\Desktop\\fl\\1\\outfile1.csv')
    print("контакт/реквизиты/эбаут  ", len(df[df.link_type2 == 'contact, requisite, about']))
    print("доставка/оплата  ", len(df[df.link_type2 == 'payment, delivery']))
    print("новости  ", len(df[df.link_type2 == 'news']))
    print("продукт  ", len(df[df.link_type2 == 'product']))
    print("логин  ", len(df[df.link_type2 == 'login']))
    print("корзина  ", len(df[df.link_type2 == 'cart']))
    print("другое  ", len(df[df.link_type2 == 'other']))
    print("2 кат  ", len(df[df.link_type2 == '2 categorys']))
    print("3 кат  ", len(df[df.link_type2 == '3 categorys']))
    return 0


function_contact_ttl()
function_contact_url()

function_requisite_ttl()
function_requisite_url()

function_about_ttl()
function_about_url()

function_payment_ttl()
function_payment_url()

function_delivery_ttl()
function_delivery_url()

function_other_ttl()
function_other_url()

function_second_sort_other()

res_ev()

TIME2 = time.perf_counter()
print('\n\n', round((TIME2 - TIME1), 3), ' seconds', sep = '')