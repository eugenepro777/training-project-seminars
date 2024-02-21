from django import forms


class GamesForm(forms.Form):
    choices = [('Coin', 'Бросить монету'), ('Dice', 'Бросить игральный кубик'), ('Number', 'Сгенерировать число')]
    action = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    quantity = forms.IntegerField(min_value=1, max_value=64)
