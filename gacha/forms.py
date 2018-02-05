from django import forms


class DashboardForm(forms.Form):

	TYPE_GAME = (
		('fate_grand_order', 'Fate Grand Order'),
		('granblue_fantasy', 'Granblue Fantasy'),
	)

	type_game = forms.ChoiceField(
		choices=TYPE_GAME,
		required=True
	)

	TYPE_GACHA = (
		('normal', 'normal'),
		('happy', 'happy'),
		('ultrahappy', 'ultrahappy'),
	)

	type_gacha = forms.ChoiceField(
		choices=TYPE_GACHA,
		required=True
	)

