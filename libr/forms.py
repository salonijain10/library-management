from django import forms  
from .models import bookdb 
class BookForm(forms.ModelForm):  
    class Meta:  
        model = bookdb  
        fields = "__all__"  