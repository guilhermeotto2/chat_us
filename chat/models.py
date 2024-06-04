from django.db import models
from django.conf import settings

class Room(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    messages = models.ManyToManyField('Message')
    created_at = models.DateTimeField(auto_now_add = True)

    """A função ForeignKey na variável user é estabelecer uma relação entre a classe Room e o modelo de usuário definido em settings.AUTH_USER_MODEL. Isso significa que cada instância de Room estará associada a um único usuário

    O cascade faz com que se o usuário for excluído, todas as rooms associadas a esse usuário tambem serão excluídas.

    O ManyToManyField faz com que um usuário possa estar associado aa muitas rooms e muitas rooms podem ter muitos usuários associados

    A presença da relação ManyToManyField com o modelo Message sugere que uma Room pode estar associada a várias mensagens. Isso implica que, para que uma Room tenha sentido em termos de aplicação, é provável que seja desejável ter pelo menos uma mensagem associada a ela. É por isso que não dá pra fazer uma room sem uma mensagem ATÉ ENTÃO.
    """

class Message(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    text = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    
    """O auto_now_add é um parâmetro que é usado para definir que, quando um objeto é criado, o campo será automaticamente preenchido com a data e hora atuais."""