from django.db import models

# Create your models here.
class News(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='news/')

    def __str__(self):
        return str(self.title)


class NewsCategory(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)

    def __str__(self):
        return str(self.category)


class NewsTags(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)

    def __str__(self):
        return str(self.tag)


class NewsComents(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=100)
    comment_author = models.CharField(max_length=100)
    commentAuthorEmail = models.EmailField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.comment_author}"  # f-string bilan chiroyli


class NewsArchives(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    archive = models.DateField()

    def __str__(self):
        return str(self.archive)
