import time
TIME1 = time.perf_counter()

import re
import pandas as pd
import numpy as np
from urllib.parse import unquote, urlparse
import pymorphy2
from pymorphy2 import tokenizers
morph = pymorphy2.MorphAnalyzer()

"""DB reading"""
df = pd.read_csv('./harvest_copy.csv')

###filtering the database from extra lines
dff = df[df.link_type != 'link_type']

###array with url types
#lt = dff.link_type.unique()
#print(lt)

###the most frequent words in the description of the url with the category "contact"
def function_contact_ttl():
    ###filter for type "contact"
    dff_contact = dff[dff.link_type == 'contact']
    ###unique descriptions for category "contact"
    ttl = dff_contact.title.unique()
    
    ###break lines into words
    ttl1 = []
    for i in range (len(ttl)-1):
        token_ttl = tokenizers.simple_word_tokenize(str(ttl[i]))
        ttl1.append(token_ttl)

    ###filter words
    ###lowercase translation
    ttl2 = []
    for i in ttl1:
        for j in i:
            ttl2.append(j.lower())

    ###remove non-letter characters and words shorter than 5 characters
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

    ###converting a word to its original form
    ttl4 = []
    for i in ttl3:
        ttl4.append(morph.parse(i)[0].normal_form)

    ###create a dictionary, key - word, value - quantity (set more than 0, can be changed)
    counter_ttl = {}
    for i in ttl4:
        counter_ttl[i] = counter_ttl.get(i, 0) + 1
    doubles_ttl = {element: count for element, count in counter_ttl.items() if count > 0}
    ttl = dict(sorted(doubles_ttl.items(), reverse = True, key=lambda x: x[1]))

    """write to file"""
    with open('./contact_title.txt','w',encoding='utf-8') as out:
        for key,val in ttl.items():
            out.write('{}:{}\n'.format(key,val))

    return 0

###the most frequent words in the url with the category "contact"
def function_contact_url():
    ###filter for type "contact"
    dff_contact = dff[dff.link_type == 'contact']
    ###unique urls for category "contact"
    url_name = dff_contact.url.unique()
    ###black list of words
    url_bl = ['html', 'php', 'asp', 'aspx', 'xhtml', 'index']
    url_name1 = []

    ###break lines into words
    for i in url_name:
        tokens = re.split('\/|\%20|-|_| |\.', unquote(urlparse(i).path))
        filtered_tokens = list(
            filter(
                lambda x: x != '' and x not in url_bl and len(x) > 3 and not x.isnumeric(), tokens
            )
        )
        for j in list(set([_token.lower() for _token in filtered_tokens])):
            url_name1.append(j)

    ###create a dictionary, key - word, value - quantity
    counter_url = {}
    for i in url_name1:
        counter_url[i] = counter_url.get(i, 0) + 1
    doubles_url = {element: count for element, count in counter_url.items() if count > 0}
    url_name = dict(sorted(doubles_url.items(), reverse = True, key=lambda x: x[1]))


    """write to file"""
    with open('./contact_url.txt','w',encoding='utf-8') as out:
        for key,val in url_name.items():
            out.write('{}:{}\n'.format(key,val))

    return 0



###the most frequent words in the description of the url with the category "payment details"
def function_requisite_ttl():
    ###filter for type "payment details"
    dff_requisite = dff[dff.link_type == 'requisite']
    ###unique descriptions for category "payment details"
    ttl = dff_requisite.title.unique()
    
    ###break lines into words
    ttl1 = []
    for i in range (len(ttl)-1):
        token_ttl = tokenizers.simple_word_tokenize(str(ttl[i]))
        ttl1.append(token_ttl)

    ###filter words
    ###lowercase translation
    ttl2 = []
    for i in ttl1:
        for j in i:
            ttl2.append(j.lower())

    ###remove non-letter characters and words shorter than 5 characters
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

    ###converting a word to its original form
    ttl4 = []
    for i in ttl3:
        ttl4.append(morph.parse(i)[0].normal_form)

    ###create a dictionary, key - word, value - quantity (set more than 0, can be changed)
    counter_ttl = {}
    for i in ttl4:
        counter_ttl[i] = counter_ttl.get(i, 0) + 1
    doubles_ttl = {element: count for element, count in counter_ttl.items() if count > 0}
    ttl = dict(sorted(doubles_ttl.items(), reverse = True, key=lambda x: x[1]))

    """write to file"""
    with open('./requisite_title.txt','w',encoding='utf-8') as out:
        for key,val in ttl.items():
            out.write('{}:{}\n'.format(key,val))

    return 0

###most frequent words in url with category "payment details"
def function_requisite_url():
    ###filter for type "payment details"
    dff_requisite = dff[dff.link_type == 'requisite']
    ###unique urls for the category "payment details"
    url_name = dff_requisite.url.unique()
    ###black list of words
    url_bl = ['html', 'php', 'asp', 'aspx', 'xhtml', 'index']
    url_name1 = []

    ###break lines into words
    for i in url_name:
        tokens = re.split('\/|\%20|-|_| |\.', unquote(urlparse(i).path))
        filtered_tokens = list(
            filter(
                lambda x: x != '' and x not in url_bl and len(x) > 3 and not x.isnumeric(), tokens
            )
        )
        for j in list(set([_token.lower() for _token in filtered_tokens])):
            url_name1.append(j)

    ###create a dictionary, key - word, value - quantity (set more than 0, can be changed)
    counter_url = {}
    for i in url_name1:
        counter_url[i] = counter_url.get(i, 0) + 1
    doubles_url = {element: count for element, count in counter_url.items() if count > 0}
    url_name = dict(sorted(doubles_url.items(), reverse = True, key=lambda x: x[1]))


    """write to file"""
    with open('./requisite_url.txt','w',encoding='utf-8') as out:
        for key,val in url_name.items():
            out.write('{}:{}\n'.format(key,val))

    return 0



###the most frequent words in the url description with the "about" category
def function_about_ttl():
    ###filtering for type "about"
    dff_about = dff[dff.link_type == 'about']
    ###unique descriptions for category "about"
    ttl = dff_about.title.unique()
    
    ###break lines into words
    ttl1 = []
    for i in range (len(ttl)-1):
        token_ttl = tokenizers.simple_word_tokenize(str(ttl[i]))
        ttl1.append(token_ttl)

    ###filter words
    ###lowercase translation
    ttl2 = []
    for i in ttl1:
        for j in i:
            ttl2.append(j.lower())

    ###remove non-letter characters and words shorter than 5 characters
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

    ###converting a word to its original form
    ttl4 = []
    for i in ttl3:
        ttl4.append(morph.parse(i)[0].normal_form)

    ###create a dictionary, key - word, value - quantity (set more than 0, can be changed)
    counter_ttl = {}
    for i in ttl4:
        counter_ttl[i] = counter_ttl.get(i, 0) + 1
    doubles_ttl = {element: count for element, count in counter_ttl.items() if count > 0}
    ttl = dict(sorted(doubles_ttl.items(), reverse = True, key=lambda x: x[1]))

    """write to file"""
    with open('./about_title.txt','w',encoding='utf-8') as out:
        for key,val in ttl.items():
                out.write('{}:{}\n'.format(key,val))

    return 0

###the most frequent words in the url with the category "about"
def function_about_url():
    ###filtering for type "about"
    dff_about = dff[dff.link_type == 'about']
    ###unique urls for category "about"
    url_name = dff_about.url.unique()
    ###black list of words
    url_bl = ['html', 'php', 'asp', 'aspx', 'xhtml', 'index']
    url_name1 = []

    ###break lines into words
    for i in url_name:
        tokens = re.split('\/|\%20|-|_| |\.', unquote(urlparse(i).path))
        filtered_tokens = list(
            filter(
                lambda x: x != '' and x not in url_bl and len(x) > 3 and not x.isnumeric(), tokens
            )
        )
        for j in list(set([_token.lower() for _token in filtered_tokens])):
            url_name1.append(j)

    ###create a dictionary, key - word, value - quantity (set more than 0, can be changed)
    counter_url = {}
    for i in url_name1:
        counter_url[i] = counter_url.get(i, 0) + 1
    doubles_url = {element: count for element, count in counter_url.items() if count > 0}
    url_name = dict(sorted(doubles_url.items(), reverse = True, key=lambda x: x[1]))


    """write to file"""
    with open('./about_url.txt','w',encoding='utf-8') as out:
        for key,val in url_name.items():
            out.write('{}:{}\n'.format(key,val))

    return 0



###the most frequent words in the description of the url with the category "payment"
def function_payment_ttl():
    ###filter for payment type
    dff_payment = dff[dff.link_type == 'payment']
    ###unique descriptions for the "payment" category
    ttl = dff_payment.title.unique()
    
    ###break lines into words
    ttl1 = []
    for i in range (len(ttl)-1):
        token_ttl = tokenizers.simple_word_tokenize(str(ttl[i]))
        ttl1.append(token_ttl)

    ###filter words
    ###lowercase translation
    ttl2 = []
    for i in ttl1:
        for j in i:
            ttl2.append(j.lower())

    ###remove non-letter characters and words shorter than 5 characters
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

    ###converting a word to its original form
    ttl4 = []
    for i in ttl3:
        ttl4.append(morph.parse(i)[0].normal_form)

    ###create a dictionary, key - word, value - quantity (set more than 0, can be changed)
    counter_ttl = {}
    for i in ttl4:
        counter_ttl[i] = counter_ttl.get(i, 0) + 1
    doubles_ttl = {element: count for element, count in counter_ttl.items() if count > 0}
    ttl = dict(sorted(doubles_ttl.items(), reverse = True, key=lambda x: x[1]))

    """write to file"""
    with open('./payment_title.txt','w',encoding='utf-8') as out:
        for key,val in ttl.items():
            out.write('{}:{}\n'.format(key,val))

    return 0

###the most frequent words in the URL with the category "payment"
def function_payment_url():
    ###filter for payment type
    dff_payment = dff[dff.link_type == 'payment']
    ###unique urls for category "payment"
    url_name = dff_payment.url.unique()
    ###black list of words
    url_bl = ['html', 'php', 'asp', 'aspx', 'xhtml', 'index']
    url_name1 = []

    ###break lines into words
    for i in url_name:
        tokens = re.split('\/|\%20|-|_| |\.', unquote(urlparse(i).path))
        filtered_tokens = list(
            filter(
                lambda x: x != '' and x not in url_bl and len(x) > 3 and not x.isnumeric(), tokens
            )
        )
        for j in list(set([_token.lower() for _token in filtered_tokens])):
            url_name1.append(j)

    ###create a dictionary, key - word, value - quantity (set more than 0, can be changed)
    counter_url = {}
    for i in url_name1:
        counter_url[i] = counter_url.get(i, 0) + 1
    doubles_url = {element: count for element, count in counter_url.items() if count > 0}
    url_name = dict(sorted(doubles_url.items(), reverse = True, key=lambda x: x[1]))


    """write to file"""
    with open('./payment_url.txt','w',encoding='utf-8') as out:
        for key,val in url_name.items():
            out.write('{}:{}\n'.format(key,val))

    return 0



###the most frequent words in the description of the url with the category "delivery"
def function_delivery_ttl():
    ###filtering for the type "delivery"
    dff_delivery = dff[dff.link_type == 'delivery']
    ###unique descriptions for the "delivery" category
    ttl = dff_delivery.title.unique()
    
    ###break lines into words
    ttl1 = []
    for i in range (len(ttl)-1):
        token_ttl = tokenizers.simple_word_tokenize(str(ttl[i]))
        ttl1.append(token_ttl)

    ###filter words
    ###lowercase translation
    ttl2 = []
    for i in ttl1:
        for j in i:
            ttl2.append(j.lower())

    ###remove non-letter characters and words shorter than 5 characters
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

    ###converting a word to its original form
    ttl4 = []
    for i in ttl3:
        ttl4.append(morph.parse(i)[0].normal_form)

    ###create a dictionary, key - word, value - quantity (set more than 0, can be changed)
    counter_ttl = {}
    for i in ttl4:
        counter_ttl[i] = counter_ttl.get(i, 0) + 1
    doubles_ttl = {element: count for element, count in counter_ttl.items() if count > 0}
    ttl = dict(sorted(doubles_ttl.items(), reverse = True, key=lambda x: x[1]))

    """write to file"""
    with open('./delivery_title.txt','w',encoding='utf-8') as out:
        for key,val in ttl.items():
            out.write('{}:{}\n'.format(key,val))

    return 0

###the most frequent words in the url with the category "delivery"
def function_delivery_url():
    ###filtering for the type "delivery"
    dff_delivery = dff[dff.link_type == 'delivery']
    ###unique urls for category "delivery"
    url_name = dff_delivery.url.unique()
    ###black list of words
    url_bl = ['html', 'php', 'asp', 'aspx', 'xhtml', 'index']
    url_name1 = []

    ###break lines into words
    for i in url_name:
        tokens = re.split('\/|\%20|-|_| |\.', unquote(urlparse(i).path))
        filtered_tokens = list(
            filter(
                lambda x: x != '' and x not in url_bl and len(x) > 3 and not x.isnumeric(), tokens
            )
        )
        for j in list(set([_token.lower() for _token in filtered_tokens])):
            url_name1.append(j)

    ###create a dictionary, key - word, value - quantity (set more than 0, can be changed)
    counter_url = {}
    for i in url_name1:
        counter_url[i] = counter_url.get(i, 0) + 1
    doubles_url = {element: count for element, count in counter_url.items() if count > 0}
    url_name = dict(sorted(doubles_url.items(), reverse = True, key=lambda x: x[1]))


    """write to file"""
    with open('./delivery_url.txt','w',encoding='utf-8') as out:
        for key,val in url_name.items():
            out.write('{}:{}\n'.format(key,val))

    return 0



###the most frequent words in the description of the url with the category "other"
def function_other_ttl():
    ###filtering for type "other"
    dff_other = dff[dff.link_type == 'other']
    ###unique descriptions for category "other"
    ttl = dff_other.title.unique()
    
    ###break lines into words
    ttl1 = []
    for i in range (len(ttl)-1):
        token_ttl = tokenizers.simple_word_tokenize(str(ttl[i]))
        ttl1.append(token_ttl)

    ###filter words
    ###lowercase translation
    ttl2 = []
    for i in ttl1:
        for j in i:
            ttl2.append(j.lower())

    ###remove non-letter characters and words shorter than 5 characters
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

    ###converting a word to its original form
    ttl4 = []
    for i in ttl3:
        ttl4.append(morph.parse(i)[0].normal_form)

    ###create a dictionary, key - word, value - quantity (set more than 0, can be changed)
    counter_ttl = {}
    for i in ttl4:
        counter_ttl[i] = counter_ttl.get(i, 0) + 1
    doubles_ttl = {element: count for element, count in counter_ttl.items() if count > 0}
    ttl = dict(sorted(doubles_ttl.items(), reverse = True, key=lambda x: x[1]))

    """write to file"""
    with open('./other_title.txt','w',encoding='utf-8') as out:
        for key,val in ttl.items():
            out.write('{}:{}\n'.format(key,val))

    return 0

###the most frequent words in the url with the category "other"
def function_other_url():
    ###filtering for type "other"
    dff_other = dff[dff.link_type == 'other']
    ###unique urls for category "other"
    url_name = dff_other.url.unique()
    ###black list of words
    url_bl = ['html', 'php', 'asp', 'aspx', 'xhtml', 'index']
    url_name1 = []

    ###break lines into words
    for i in url_name:
        tokens = re.split('\/|\%20|-|_| |\.', unquote(urlparse(i).path))
        filtered_tokens = list(
            filter(
                lambda x: x != '' and x not in url_bl and len(x) > 3 and not x.isnumeric(), tokens
            )
        )
        for j in list(set([_token.lower() for _token in filtered_tokens])):
            url_name1.append(j)

    ###create a dictionary, key - word, value - quantity (set more than 0, can be changed)
    counter_url = {}
    for i in url_name1:
        counter_url[i] = counter_url.get(i, 0) + 1
    doubles_url = {element: count for element, count in counter_url.items() if count > 0}
    url_name = dict(sorted(doubles_url.items(), reverse = True, key=lambda x: x[1]))


    """write to file"""
    with open('./other_url.txt','w',encoding='utf-8') as out:
        for key,val in url_name.items():
            out.write('{}:{}\n'.format(key,val))

    return 0



###re-sorting of sites with the category "other"
def function_second_sort_other():
    ###create an empty file for writing lines
    with open('./outfile1.csv', 'w'):
        pass

    ###filtering for type "other"
    dff_other = dff[dff.link_type == 'other']

    ###black list of words
    url_bl = ['html', 'php', 'asp', 'aspx', 'xhtml', 'index']

    ###keywords and word blacklists for all categories
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
    

    ### Combine all groups of urls into one dictionary
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
    

    ###break lines into words
    dff_other = dff_other.reindex(dff_other.columns.to_list() + ['link_type2'], axis=1)
    print(len(dff_other))
    quant_str = 1
    ###timer for 1000 lines
    count = 0
    start = int(time.time())
    dff_other1 = dff_other.head(0)
    dff_other1.to_csv('./outfile1.csv', mode = 'a', index = False)
    for strings in range (1, len(dff_other), quant_str):
        count += 1
        if count % 1000 == 0:
                now = int(time.time())
                print(count, now - start)
                start = int(time.time())
        ###create df with one line, because line by line works faster
        dff_other_cycle = pd.concat([dff_other.head(0), dff_other[strings:strings+quant_str]], ignore_index = True)
        
        ###word counter in url and description, a new one is created for each line
        categories_counter = {
                'contact, requisite, about': 0, 
                'payment, delivery': 0, 
                'news': 0, 
                'product': 0, 
                'login': 0, 
                'cart': 0
            }
        
        ###split url into words
        for adress in dff_other_cycle.url:
            tokens = re.split('\/|\%20|-|_| |\.', unquote(urlparse(adress).path))
            filtered_tokens = list(
                filter(
                    lambda x: x != '' and x not in url_bl and len(x) > 3 and not x.isnumeric(), tokens
                )
            )
        
        ###we break the description into words, reduce it to lowercase and into the initial form, remove all unnecessary characters
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

        ###Declaring a dictionary with counters
        
        for j in list(set([_token.lower() for _token in filtered_tokens])):
            for _url_group_name, _url_group_list in url_groups.items():
                if j in _url_group_list:
                    categories_counter[_url_group_name] += 1

        ###similar to the previous one, but for the blacklist
        ###since this is a blacklist, then the counter is minus by a more significant value
        ###so that the inclusion of this word clearly shows that the url is not related to the category
        for j in list(set([_token.lower() for _token in filtered_tokens])):
            for _url_group_name_bl, _url_group_list_bl in url_groups_bl.items():
                if j in _url_group_list_bl:
                    categories_counter[_url_group_name_bl] -= 5
        
        ###similar to the previous one
        for j in ttl4:
            for _title_group_name, _title_group_list in title_groups.items():
                if j in _title_group_list:
                    categories_counter[_title_group_name] += 1
        
        ###similar to the previous one
        for j in ttl4:
            for _title_group_name_bl, _title_group_list_bl in title_groups_bl.items():
                if j in _title_group_list_bl:
                    categories_counter[_title_group_name_bl] -= 5

        ###the variable max_category_name will store the name of the category (url_contact, url_news) with the maximum counter
        max_category_name = max(categories_counter, key=categories_counter.get)
        ###this list is needed to evaluate misassignment (2-3 categories with the same counter)
        sorted_categories_counter = list(sorted(categories_counter.items(), key = lambda item: item[1], reverse = True))
        ###category assignment
        if sorted_categories_counter[0][1] == sorted_categories_counter[1][1] == sorted_categories_counter[2][1] != 0:
            dff_other_cycle.loc[dff_other_cycle['url'] == adress, 'link_type2'] = '3 categorys'
        elif sorted_categories_counter[0][1] == sorted_categories_counter[1][1] != 0:
            dff_other_cycle.loc[dff_other_cycle['url'] == adress, 'link_type2'] = '2 categorys'
        elif sorted_categories_counter[0][1] != 0:
            dff_other_cycle.loc[dff_other_cycle['url'] == adress, 'link_type2'] = max_category_name
        else:
            dff_other_cycle.loc[dff_other_cycle['url'] == adress, 'link_type2'] = 'other'
        
        ###write to file line by line
        dff_other_cycle.to_csv('./outfile1.csv', mode = 'a', index = False, header = False)
    
    return 0
    
###evaluating the results of the resort function
def res_ev():
    df = pd.read_csv('./outfile1.csv')
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
