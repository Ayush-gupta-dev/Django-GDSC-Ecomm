from django import forms 
from .models import Item

FORM_CLASS = 'w-full m-2 px-4 py-2 rounded-xl border text-slate-700'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields=('category','priority_tag','name','description','price','image')
        widgets={
            'category': forms.Select(attrs={
                'class':FORM_CLASS
            }),
            'priority_tag': forms.Select(attrs={
                'class':FORM_CLASS
            }),
            'name': forms.TextInput(attrs={
                'class':FORM_CLASS
            }),
            'description': forms.Textarea(attrs={
                'class':FORM_CLASS,'rows':6,'cols':20,'style': 'resize: none;'
            }),
            'price': forms.TextInput(attrs={
                'class':FORM_CLASS
            }),
            'image': forms.FileInput(attrs={
                'class':'w-full m-2 px-4 py-2 rounded-xl border bg-slate-200 text-slate-700'
            })
        }
        