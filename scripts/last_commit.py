from collections import namedtuple
from pprint import pprint
from bs4 import BeautifulSoup as bs
from requests import get
import json
import unicodedata
import re
import time


def load_url_parser(url):
    """Carrega o parse do site."""
    site = get(url)
    time.sleep(1)
    return bs(site.text, 'html.parser')


def load_list(file):
    f = open(file, 'r')
    links = []
    for linha in f.readlines():
        links.append(linha.strip())
    f.close()
    return links


list_project = load_list('list_project2.txt')

# url = 'https://github.com/gujjwal00/avnc'
# site = load_url_parser(url)
# # boxes = site.find_all('relative-time', {'class': 'no-wrap'})
# print(site.find('relative-time').text)
cont = 0
err = []
for line in list_project:

    if "github" in line:
        cont += 1
        # print(line)
        site = load_url_parser(line)
        try:
            print(site.find('relative-time').text)

        except AttributeError:
            print_err = True
            time_ago_list = site.find_all('time-ago')
            # if len(time_ago_list) == 0:
            #     time.sleep(1)
            #     site = load_url_parser(line)
            #     time_ago_list = site.find_all('time-ago')
            # if len(time_ago_list) == 0:
            #     time.sleep(3)
            #     site = load_url_parser(line)
            #     time_ago_list = site.find_all('time-ago')
            # if len(time_ago_list) == 0:
            #     time.sleep(8)
            #     site = load_url_parser(line)
            #     time_ago_list = site.find_all('time-ago')

            for time_ago in time_ago_list:
                # print("ssssssssssssssss",time_ago.text)
                if '2023' in time_ago.text:
                    print(">>",time_ago.text)
                    print_err = False
                    break

            # for time_ago in time_ago_list:
            #     if '2020' in time_ago.text:
            #         print(">>",time_ago.text)
            #         print_err = False
            #         break

            # for time_ago in time_ago_list:
            #     if '2019' in time_ago.text:
            #         print(">>",time_ago.text)
            #         print_err = False
            #         break
            #
            #     if '2018' in time_ago.text:
            #         print(">>",time_ago.text)
            #         print_err = False
            #         break
            #     if '2017' in time_ago.text:
            #         print(">>",time_ago.text)
            #         print_err = False
            #         break
            if print_err:
                print('erro')
                err.append(line)

    else:
        print('none')

print(cont)


# with open("output2.html", "w") as file:
#     file.write(str(site))
