from django import forms
from . models import *

class OrginizationForm(forms.ModelForm):
    class Meta:
        model = Orginization
        fields = ('name','description')
        widgets = {
        'name': forms.TextInput(attrs={'placeholder':'name','id':'ccc'}),
        'description': forms.TextInput(attrs={'placeholder':'Description','id':'cc'}),
        }






        # ('Orginization_name','emp_id','full_name','father_name','designation','created_by')

class EmpolyeeForm(forms.ModelForm):
    class Meta:
        model = Empolyee
        fields = ('emp_id','Orginization_name','full_name','father_name','designation','created_by','id_card_NO',
                    'volume_NO','page_NO','all_contacts','id_card_pic','emp_pic')

        widgets = {
            'emp_id':forms.TextInput(attrs={'placeholder':'emp id','id':'em1'}),
            'Orginization_name':forms.Select(attrs={'placeholder':'orginization','id':'em2'}),
            'full_name':forms.TextInput(attrs={'placeholder':'full name','id':'em3'}),
            'father_name':forms.TextInput(attrs={'placeholder':'father name','id':'em4'}),
            'designation':forms.TextInput(attrs={'placeholder':'designation','id':'em5'}),
            'created_by':forms.Select(attrs={'placeholder':'orginization','id':'em6'}),
            'id_card_NO':forms.TextInput(attrs={'placeholder':'designation','id':'em7'}),
            'volume_NO':forms.TextInput(attrs={'placeholder':'designation','id':'em8'}),
            'page_NO':forms.TextInput(attrs={'placeholder':'designation','id':'em9'}),
            'all_contacts':forms.TextInput(attrs={'placeholder':'designation','id':'em10'}),

        }
class IdentifyCreateForm(forms.ModelForm):
    class Meta:
        model = Identify
        fields = ('empoly','gsm','full_ismi')


        widgets = {
            'empoly':forms.Select(attrs={'class':'form-control','id':'iden1'}),
            'gsm':forms.TextInput(attrs={'class':'form-control','placeholder':'GSM','id':'iden2'}),
            'full_ismi':forms.TextInput(attrs={'class':'form-control','placeholder':'Full ISMI','id':'iden3'}),

        }
