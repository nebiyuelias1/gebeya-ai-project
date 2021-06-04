from django.forms import ModelForm, Textarea

from views.models import View


class ViewForm(ModelForm):

    class Meta:
        model = View
        fields = ['content']
        labels = {
            "content": "",
        }
        widgets = {
            'content': Textarea(attrs={'rows': 2, 'placeholder': 'Speak your mind...'}),
        }
