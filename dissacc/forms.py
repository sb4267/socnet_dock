from django import forms
from . models import *
from . dis_clsss import *
class dis_cls_names(forms.ModelForm):

    type3=dis_nms()


    dis_class=forms.ChoiceField(choices=type3,required=True,label='Disease Type 1')
    dis_clss_2=forms.ChoiceField(choices=type3,required=True,label='Disease Type 2')

    class Meta:
        model = Main_table
        fields = [
        'dis_class',
        'dis_clss_2'
        ]
