from django.forms import ModelForm
from .models import File
from django.contrib.auth.forms import User

class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['title', 'comment', 'file']

class UserChangeForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'