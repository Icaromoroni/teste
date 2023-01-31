from django.db import models


# calsses modelos

SEXO = (('M','Masculino'), ('F', 'Feminino'))

STATUS_INFECTADO = (('n', 'Não'), ('s', 'Sim'))

class Cadastros(models.Model):

    nome = models.CharField(max_length=100)

    idade = models.CharField(max_length=10)

    sexo = models.CharField(max_length=1, choices=SEXO, blank=True, null=False)

    latitude = models.IntegerField(default=None,blank=True, null=False)
    
    longitude = models.IntegerField(default=None,blank=True, null=False)

    status_infectado = models.CharField(max_length=1, default='n', choices=STATUS_INFECTADO)
    
    def __str__(self) -> str:
        return self.nome

class Itens(models.Model):

    nome = models.CharField(max_length=50)
    
    ponto = models.IntegerField()

    def __str__(self) -> str:
        return self.nome

class Inventario(models.Model):

    cadastro_id = models.ForeignKey (Cadastros, on_delete=models.CASCADE)

    itens_id = models.ForeignKey (Itens, on_delete=models.CASCADE)

    quantidade = models.IntegerField()




