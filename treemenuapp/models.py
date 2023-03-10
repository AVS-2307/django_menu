from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Rubric(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='children')  # ссылается на ту же модель Rubric, на поле id

    def __str__(self):  # строковое представление для админки
        return self.name

    # ссылки каждой рубрики
    def get_absolute_url(self):
        return reverse('rubric', kwargs={'pk': self.pk})

    class MPTTMeta:
        order_insertion_by = ['name']
