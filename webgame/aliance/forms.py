from django import forms

class UploadFileForm(forms.Form):

    ali_view = forms.FileField(
        label="Přehled Aliance",
        required=False,
        widget= forms.FileInput(attrs={'accept' : '.html'}),
    )
    ali_detail = forms.FileField(
        label="Detaily Aliance",
        required=False,
        widget= forms.FileInput(attrs={'accept' : '.html'}),
    ) # required True
    
    def clean_ali_view(self):
        file = self.cleaned_data.get('ali_view')
        if file and not file.name.endswith('.html'):
            raise ValidationError("Soubor musí mít koncovku .html")
        return file
    
    def clean_ali_detail(self):
        file = self.cleaned_data.get('ali_detail')
        if file and not file.name.endswith('.html'):
            raise ValidationError("Soubor musí mít koncovku .html")
        return file