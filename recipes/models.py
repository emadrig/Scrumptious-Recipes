from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    picture = models.URLField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title


class RecipeStep(models.Model):
    step_number = models.SmallIntegerField()
    instruction = models.TextField()

    recipe = models.ForeignKey(
        "Recipe",
        related_name="steps",
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["step_number"]
