import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import collections
from itertools import combinations
def dis_nms():
    main_csv = pd.read_csv("./data/final.csv", encoding="iso8859-1")

    new_dict= collections.defaultdict(list)

    for k, items in main_csv.iterrows():
        if main_csv.iloc[k][2] in new_dict:
            new_dict[main_csv.iloc[k][2]].update({main_csv.iloc[k][1]: [i.strip() for i in main_csv.iloc[k][3].split(',')]})
        else:
            new_dict[main_csv.iloc[k][2]]={main_csv.iloc[k][1]: [i.strip() for i in main_csv.iloc[k][3].split(',')]}


    all_classes={}
    for cls in new_dict.keys():
        cntr_comb=collections.Counter()
        dis_list=[]
        for d in new_dict[cls]:
            dis_list.append(d)
        c=combinations(dis_list,2)
        for com in c:
            a_list=[]
            for i in new_dict[cls][com[0]]:
                a_list.append(i)
            b_list=[]
            for i in new_dict[cls][com[1]]:
                b_list.append(i)

            for i in a_list:
                for j in b_list:
                    if i==j:
                        cntr_comb[(com[0],com[1])]+=1
        all_classes[cls]=cntr_comb

    lst_dict={}
    for cls in all_classes:
        lst=[]
        for i in all_classes[cls]:
            lst.append([i[0],i[1],all_classes[cls][i]])
        lst_dict[cls]=lst

    brands=[]
    for i in lst_dict.keys():
        brands.append((i,i))
    return brands
