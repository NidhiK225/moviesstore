from django.db import models
from movies.models import Movie
from django.contrib.auth.models import User

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id) + ' - ' + self.user.username

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id) + ' - ' + self.movie.name

class CheckoutStatement(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="statement")
    name = models.CharField(max_length=100, blank=True, null=True)
    thoughts = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Statement for Order {self.order.id} by {self.name or 'Anonymous'}"
