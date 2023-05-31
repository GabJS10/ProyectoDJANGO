from django import forms


class formContacto(forms.Form):

    nombre = forms.CharField(label="nombre", required=True)
    email = forms.EmailField(label='email',required=True)
    contenido = forms.CharField(label="contenido",widget=forms.Textarea)
