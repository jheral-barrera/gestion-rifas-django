from django import forms

from .models import Rifa, Premio, Compra, Numero

class RifaForm(forms.ModelForm):
    class Meta:
        model = Rifa
        fields = '__all__'

        widgets = {
            'nombre_rifa': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion_rifa': forms.Textarea(attrs={'class': 'form-control'}),
            'fecha_inicio_rifa': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_termino_rifa': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cantidad_numeros_rifa': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado_rifa': forms.Select(attrs={'class': 'form-control'}),
        }


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'

        widgets = {
            'nombre_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'email_cliente': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono_cliente': forms.NumberInput(attrs={'class': 'form-control'}),
            'codigo_pago': forms.TextInput(attrs={'class': 'form-control'}),
            'rifa': forms.Select(attrs={'class': 'form-control'}),
        }

    # def clean_nombre_cliente(self):
    #     nombre_cliente = self.cleaned_data['nombre_cliente']
    #     rifa = self.cleaned_data['rifa']
    #     if Compra.objects.filter(nombre_cliente=nombre_cliente, rifa=rifa).exists():
    #         raise forms.ValidationError("Este cliente ya existe.")
    #     return nombre_cliente

class PremioForm(forms.ModelForm):
    class Meta:
        model = Premio
        fields = '__all__'
        
        widgets = {
            'nombre_premio': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion_premio': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen_premio': forms.FileInput(attrs={'class': 'form-control'}),
            'comprador': forms.HiddenInput(),
            'rifa': forms.Select(attrs={'class': 'form-control'}),
        }

class NumeroForm(forms.ModelForm):
    class Meta:
        model = Numero
        fields = '__all__'

        widgets = {
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'codigo_pago': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_pago': forms.HiddenInput(),
            'comprador': forms.Select(attrs={'class': 'form-control'}),
            'rifa': forms.Select(attrs={'class': 'form-control'})
        }

    # E
        
    def clean_codigo_pago(self):
        codigo_pago = self.cleaned_data['codigo_pago']

        if not codigo_pago:
            return codigo_pago
        if len(codigo_pago) != 10:
            raise forms.ValidationError('El código de pago debe tener 10 dígitos :(')
        if not codigo_pago[:3].isalpha():
            raise forms.ValidationError('El codigo de pago debe tener los primeros 3 caracteres deben ser alfabéticos :(')
        if not codigo_pago[3:].isdigit():
            raise forms.ValidationError('El codigo de pago debe tener los últimos 7 caracteres deben ser numéricos :(')

        ultimos_numeros = list(map(int, codigo_pago[3:]))
        pares = sum(1 for num in ultimos_numeros if num % 2 == 0)
        impares = len(ultimos_numeros) - pares
        if impares >= pares:
            raise forms.ValidationError('El codigo de pago debe haber mas numeros pares que impares en los ultimos 7 digitos')

        return codigo_pago