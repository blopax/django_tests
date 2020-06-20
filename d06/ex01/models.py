from django.contrib.auth.models import User, Permission
from django.db import models

# Create your models here.

class TipUser(User):
    def update_perms(self):
        permission = Permission.objects.get(name='can downvote')
        try:
            user_tips = Tip.objects.filter(auteur=self)
            upvotes = user_tips.aggregate(models.Sum('upvotes'))
            downvotes = user_tips.aggregate(models.Sum('downvotes'))
            print(f"{upvotes} up and {downvotes} down")
            if upvotes['upvotes__sum'] > downvotes['downvotes__sum']:
                self.user_permissions.add(permission)
            else:
                self.user_permissions.remove(permission)
        except:
            self.user_permissions.remove(permission)



class Tip(models.Model):
    contenu = models.TextField()
    auteur = models.ForeignKey('TipUser', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    class Meta:
        permissions = (
            ("can_downvote", "can downvote"),
            )


class Vote(models.Model):
    voter = models.ForeignKey('TipUser', on_delete=models.CASCADE)
    tip = models.ForeignKey('Tip', on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
