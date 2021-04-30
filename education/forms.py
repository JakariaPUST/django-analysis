from django import forms
from .models import Contact, Post

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class ContactForm2(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label="My Name"
        self.fields['name'].initial="My Name"
        self.fields['email'].label="My Email"
        self.fields['email'].initial="Email"

    def clean_name(self):
        value=self.cleaned_data.get('name')
        num_Of_word=value.split(' ')
        if len(num_Of_word) > 3:
            self.add_error('name', "Name can have max 3 words")
        else:
            return value




        #uncomment if we want form as look like with model form

        # widgets ={
        #     'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Name..'}),
        #     'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Email..'}),
        #     'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Phone..'}),
        #     'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Say something...','rows':3}),
        # }
        # labels ={
        #     'name' : 'Your Name',
        #     'email' : 'Your Email',
        #     'phone' : 'Your phone',
        #     'content' : 'Your Content',

        # }
        # help_texts ={
        #     'name' : 'Your helo name',
        #     'email' : 'Your email help',
        #     'phone' : 'Your phoone',
        #     'content' : 'Your help Content',

        # }
from .fields import ListTextWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','id','created_at','slug','likes', 'views']
        widgets ={
            'class_in':forms.CheckboxSelectMultiple(attrs={
                'multiple':True,
            }),
            'subject':forms.CheckboxSelectMultiple(attrs={
                'multiple':True,
            })
        }
    def __init__(self,*args, **kwargs):
        _district_set=kwargs.pop('district_set',None)
        super(PostForm,self).__init__(*args,**kwargs)
        self.fields['district'].widget=ListTextWidget(data_list=_district_set, name='district-set')


from .models import PostFile
class FileModelForm(forms.ModelForm):
    class Meta:
        model = PostFile
        fields = ['image']