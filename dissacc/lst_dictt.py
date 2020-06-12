import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import collections
from itertools import combinations
def nxs(attr1,attr2):
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

    comb_dict= collections.defaultdict(list)

    for k, items in main_csv.iterrows():
        if main_csv.iloc[k][2] in comb_dict:
            comb_dict[main_csv.iloc[k][2]].update({str(main_csv.iloc[k][2])+'_'+str(main_csv.iloc[k][1]): [i.strip() for i in main_csv.iloc[k][3].split(',')]})
        else:
            comb_dict[main_csv.iloc[k][2]]={str(main_csv.iloc[k][2])+'_'+str(main_csv.iloc[k][1]): [i.strip() for i in main_csv.iloc[k][3].split(',')]}

    import itertools
    main_comb_dict={}
    comb_dis_me=[attr1,attr2]
    com_ddict_c13=combinations(comb_dis_me,2)
    for e in com_ddict_c13:
        dic_comb= collections.Counter()
        set_lst=[i for i in new_dict[e[0]].keys()]
        set_lst_nerv=[i for i in new_dict[e[1]].keys()]
        a = [set_lst,set_lst_nerv]
        prd_lst=list(itertools.product(*a))
        for each in prd_lst:
            a_list=[]
            for item in new_dict[e[0]]:
                if item in each[0]:
                    for gene1 in new_dict[e[0]][each[0]]:
                        a_list.append(gene1)
            b_list=[]
            for item in new_dict[e[1]]:
                if item in each[1]:
                    for gene2 in new_dict[e[1]][each[1]]:
                        b_list.append(gene2)
            for i in a_list:
                for j in b_list:
                    if i==j:
                        dic_comb[(each[0],each[1])]+=1
        main_comb_dict[(str(e[0])+'_'+str(e[1]))]=dic_comb
    lst=[]
    for combi in main_comb_dict:
        for i in main_comb_dict[combi]:
            lst.append([i[0],i[1],main_comb_dict[combi][i]])
    return lst_dict,lst
