from django.forms import ModelForm
from ..models import TipUser, Tip


class TipForm(ModelForm):
    class Meta:
        model = Tip
        fields = ['contenu']

    def save_tip(self, username):
        contenu = self.cleaned_data['contenu']
        auteur = TipUser.objects.get(username=username)
        new_tip = Tip(auteur=auteur, contenu=contenu)
        new_tip.save()
