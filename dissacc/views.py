import os
from PIL import Image

from django.shortcuts import render
from .forms import *
from . lst_dictt import *
from django.http import HttpResponse
from http.client import responses
from django.shortcuts import redirect
import random,string

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
# Create your views here.
def home(request):
    import networkx
    import matplotlib.pyplot as plt
    if request.method == 'POST':
        form = dis_cls_names(request.POST)
        if form.is_valid():
            global x
            global varG2
            global dis_class1
            global dis_class2
            dis_class1 = form.cleaned_data.get('dis_class')
            dis_class2 = form.cleaned_data.get('dis_clss_2')
            get_lst,lst=nxs(dis_class1,dis_class2)
            x=randomString()
            for i in range(3):
                G = nx.DiGraph()
                if i==0:
                    for d in get_lst[dis_class1]:
                        G.add_edge(d[0],d[1],weight=d[2])
                    # networkx.drawing.nx_agraph.graphviz_layout(G, prog='neato', root=None, args='')
                    nx.draw(G,with_labels=True, edge_color='b',arrows=True,node_color='r',alpha=0.75)
                    med_str="media/images/"+'1'+x+".png"
                    import matplotlib.pyplot as plt
                    plt.savefig(med_str)
                elif i==1:
                    for e in get_lst[dis_class2]:
                        G.add_edge(e[0],e[1],weight=e[2])
                    # networkx.drawing.nx_agraph.graphviz_layout(G, prog='neato', root=None, args='')
                    nx.draw(G,with_labels=True, edge_color='b',arrows=True,node_color='r',alpha=0.75)
                    med_str1="media/images/"+'2'+x+".png"
                    import matplotlib.pyplot as plt
                    plt.savefig(med_str1)
                elif i==2:

                    for e in lst:
                        G.add_edge(e[0],e[1],weight=e[2])
                    # networkx.drawing.nx_agraph.graphviz_layout(G, prog='neato', root=None, args='')
                    nx.draw(G,with_labels=True, edge_color='b',arrows=True,node_color='r',alpha=0.75)
                    med_str2="media/images/"+'3'+x+".png"
                    import matplotlib.pyplot as plt
                    plt.savefig(med_str2)

                plt.clf()
                G.clear()
        return redirect('thi_img')

    else:
        u_form = dis_cls_names()
    context = {'u_form': u_form,}
    return render(request, 'home.html',context)

def final_imgs(request):

    img_1= os.path.join('/media/images/', '1'+x+'.png')
    img_2=os.path.join('/media/images/', '2'+x+'.png')
    img_3=os.path.join('/media/images/', '3'+x+'.png')
    return render(request, 'new1.html',context={'img_1':img_1,
    'img_2':img_2,
    'img_3':img_3,
    'comb':str(dis_class1)+' and '+str(dis_class2),
    'v1':dis_class1,
    'v2':dis_class2})
