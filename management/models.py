from django.db import models
from django.contrib.auth.models import User 

class Book(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    ISBN = models.IntegerField()
    publication_date = models.DateField(auto_now_add=True,blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    availability = models.IntegerField()

    def __str__(self):
        return f"{self.title} - {self.author}"





class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user','book')
    def __str__(self):
        return f"{self.user}-{self.book.id}"
    


class Borrowing(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateTimeField(auto_now=True,null=True,blank=True)
    def __str__(self):
        return f"{self.user}-{self.book}-{self.return_date}"
    class Meta:
        unique_together = ('user','book')