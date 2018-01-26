from django.db import models

from django.contrib.auth.models import User

# Create your models here


class Session(models.Model):
    key = models.CharField(unique=True, max_length=100)
    user = models.ForeignKey(User)
    expires = models.DateTimeField()


#-----------------------------------------------------------------#




class Profile(models.Model):
    avatar = models.ImageField(upload_to='uploads/')
    usr_key = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.usr_key.username



#-----------------------------------------------------------------#



class Tag(models.Model):
    tag_text = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag_text

    class Meta:
        ordering = ('tag_text',)



#-----------------------------------------------------------------#


class Question(models.Model):
    header = models.CharField(max_length=50)
    text = models.TextField(max_length=510)
    author = models.ForeignKey(Profile)
    tags = models.ManyToManyField(Tag)
    # def __str__(self):
    #     return self.header

    # сделать рейтинг и транзакции
    def likes(self):
        return Like.objects.filter(question_key=self, rate=True).count()

    def dislikes(self):
        return Like.objects.filter(question_key=self, rate=False).count()

#-----------------------------------------------------------------#





class Answer(models.Model):
    text = models.TextField(max_length=510)
    correct = models.BooleanField(default=False)
    author = models.ForeignKey(Profile)






#-----------------------------------------------------------------#





class Like(models.Model):
    question_key = models.ForeignKey(Question)
    like_author = models.ForeignKey(User)
    rate = models.BooleanField(default=None)

    class Meta:
        unique_together= ['question_key', 'like_author']




#-----------------------------------------------------------------#