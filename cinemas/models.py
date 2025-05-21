from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, default='now')

    def __str__(self):
        return str(self.name)


class Cinemas(models.Model):
    title = models.CharField(max_length=100)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)]
    )
    duration = models.IntegerField()
    description = models.TextField()
    language = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cinema_youtube_link = models.URLField(default='https://www.youtube.com/watch?v=')
    def average_rating(self):
        avg = self.cinemacoments_set.aggregate(Avg('rating'))['rating__avg']
        return round(avg, 1) if avg else 0
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class CinemaArchives(models.Model):
    cinema = models.ForeignKey(Cinemas, on_delete=models.CASCADE)
    archive = models.DateField()

    def __str__(self):
        return str(self.archive)


class CinemaGenres(models.Model):
    cinema = models.ForeignKey(Cinemas, on_delete=models.CASCADE)
    genre_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.genre_name)


class CinemaReleaseDate(models.Model):
    cinema = models.ForeignKey(Cinemas, on_delete=models.CASCADE)
    release_date = models.DateField()

    def __str__(self):
        return str(self.release_date)


class CinemaDirecters(models.Model):
    cinema = models.ForeignKey(Cinemas, on_delete=models.CASCADE)
    director_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.director_name)


class CinemaStars(models.Model):
    cinema = models.ForeignKey(Cinemas, on_delete=models.CASCADE)
    star_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.star_name)


class CinemaProductCompony(models.Model):
    cinema = models.ForeignKey(Cinemas, on_delete=models.CASCADE)
    product_compony = models.CharField(max_length=100)

    def __str__(self):
        return str(self.product_compony)


class CinemaCountry(models.Model):
    cinema = models.ForeignKey(Cinemas, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)

    def __str__(self):
        return str(self.country)


class CinemaTags(models.Model):
    cinema = models.ForeignKey(Cinemas, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)

    def __str__(self):
        return str(self.tag)


class CinemaComents(models.Model):
    cinema = models.ForeignKey(Cinemas, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=100)
    comment_author = models.CharField(max_length=100)
    commentAuthorEmail = models.EmailField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.comment_author}"


class CinemaImages(models.Model):
    cinema = models.ForeignKey(Cinemas, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cinemas/')

    def __str__(self):
        return str(self.image.url) if self.image else "No Image"

class CinemaPhotos(models.Model):
    cinema = models.ForeignKey(Cinemas, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='cinemas/photos/')
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)