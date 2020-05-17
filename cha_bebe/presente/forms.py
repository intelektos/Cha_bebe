from django import forms

class Adicionar_ao_carrinho(forms.Form):
    quantidade = forms.IntegerField(widget=forms.TextInput(attrs={'size':'2', 'value':'1', 'class':'quantity'}),
                                  error_messages={'Inválido':'Insira uma quantidade válida. (mínimo 1)'},
                                  min_value=1)
    presente_slug = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, request=None, *args, **kwargs):
        """ override the default so we can set the request """
        self.request = request
        super(Adicionar_ao_carrinho, self).__init__(*args, **kwargs)

    def clean(self):
        """ custom validation to check for presence of cookies in customer's browser """
        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError("Cookies precisam estar habilitados.")
        return self.cleaned_data
