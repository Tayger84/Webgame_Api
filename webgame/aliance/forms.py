from django import forms

class Upload(forms.Form):
    # title = forms.CharField(max_length=100, required=False)
    ali_view = forms.FileField(
        label="Přehled Aliance",
        required=False,
        widget= forms.FileInput(attrs={'accept' : '.html'}),
    )
    ali_detail = forms.FileField(
        label="Detaily Aliance",
        required=True,
        widget= forms.FileInput(attrs={'accept' : '.html'}),
    )
    
    def clean_html_file(self):
        file = self.cleaned_data['html_file']
        if not file.name.endswith('.html'):
            raise forms.ValidationError("Soubor musí mít příponu .html")
        if file.content_type != 'text/html':
            raise forms.ValidationError("Soubor není platný HTML dokument")
        file.seek(0)
        return file