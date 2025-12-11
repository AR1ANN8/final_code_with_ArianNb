from tkinter import *
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
window = Tk()
window.geometry("400x400")
window.title("ArianNb")
def my_function(file_name: str):
    with open(f'{file_name}.html', 'r') as f:
        html_page = f.read()
    content = BeautifulSoup(html_page, 'html.parser', encoding = 'utf-8') #utf-8 between cotations for persian language
    # print(content)
    item_info = content.findall("td")
    my_lst = []
    for i in item_info:
        my_lst.append(i)
        # print(my_lst)
    k = 4
    item_lst = []
    for j in range(0, len(my_lst), 4):
        item = my_lst[j:k]
        item_name = item[0].string
        item_price = item[1].string
        item_category = item[2].string
        item_count = item[3].string
        tpl = (item_name, item_price, item_category, item_count)
        item_lst.append(tpl)
        k += 4
    df = DataFrame(item_lst, columns = ['name', 'price', 'category', 'count'])
    print(df)
    df.to_csv("item_info.csv")
btn = Button(text = "Click me!", command = my_function)
btn.pack()
window.mainloop()
