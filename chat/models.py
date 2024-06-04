from django.db import models
from django.conf import settings

class Room(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    messages = models.ManyToManyField('Message', blank=True)
    created_at = models.DateTimeField(auto_now_add = True)

    """A função ForeignKey na variável user é estabelecer uma relação entre a classe Room e o modelo de usuário definido em settings.AUTH_USER_MODEL. Isso significa que cada instância de Room estará associada a um único usuário

    O cascade faz com que se o usuário for excluído, todas as rooms associadas a esse usuário tambem serão excluídas.

    O ManyToManyField faz com que um usuário possa estar associado aa muitas rooms e muitas rooms podem ter muitos usuários associados.
    Por padrão ele vem com null=true, mas blank=false, tem que deixar como True para que vc possa criar uma room sem mensagem obrigatoria

    """

class Message(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    text = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    
    """O auto_now_add é um parâmetro que é usado para definir que, quando um objeto é criado, o campo será automaticamente preenchido com a data e hora atuais."""