from django.db import models
from django.utils.timezone import now
from PIL import Image
from django.utils.text import slugify
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User


#custom model manager

class PostManager(models.Manager):
    def sorted(self,title):
        return self.order_by(title)
    def less_than(self,size):
        return self.filter(salary__lt=size)


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    content = models.TextField()

    def __str__(self):
        return self.name

class Subject(models.Model):
    name= models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_total_post_count(self):
        return self.subject_set.all().count()
    def get_total_post_list(self):
        return self.subject_set.all()
class Classs_in(models.Model):
    name= models.CharField(max_length=100)
    def __str__(self):
        return self.name



class District(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

        

class Post(models.Model):
    CATEGORY={
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    }
    MEDIUM =(
        ('bangla', 'bangla'),
        ('english', 'english'),
        ('hindi', 'hindi'),
        ('mandarin', 'mandarin'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, default=title)
    email = models.EmailField()
    salary = models.FloatField()
    details = models.TextField()
    available = models.BooleanField()
    category = models.CharField(max_length=100, choices=CATEGORY)
    created_at = models.DateTimeField(default=now)
    image = models.ImageField(default="default.jpg", upload_to="education/images")

    medium = MultiSelectField(max_length=100, max_choices=4, choices=MEDIUM, default='english')
    
    subject=models.ManyToManyField(Subject,related_name='subject_set')

    class_in=models.ManyToManyField(Classs_in,related_name='class_set')

    likes= models.ManyToManyField(User, related_name='like_set')
    views= models.ManyToManyField(User, related_name='view_set')
    def total_likes(self):
        return self.likes.count() 
    def total_views(self):
        return self.views.count() 

    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        img= Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size= (300,300)
            img.thumbnail (output_size)
            img.save(self.image.path)
    def __str__(self):
        return self.title + " by: " + self.user.username
    def get_subject_name(self):
        sub=self.subject.all()
        subjects=""
        for i in sub:
            subjects = subjects + str(i.name) + ", "
        return subjects
    def get_class_name(self):
        sub=self.class_in.all()
        classes=""
        for i in sub:
            classes = classes + str(i.name) + ", "
        return classes
    def proppercase(self):
        return self.title.title()
    def uppercase(self):
        return self.title.upper()

    def details_short(self):
        details_words=self.details.split(' ')
        if len(details_words) >10:
            return ' '.join(details_words[:10])+ "..."
        else:
            return self.details
        
    objects=models.Manager() #buildin manager
    items=PostManager() #Custom manager








class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=now)
    def __str__(self):
        return self.user.username + ": " + self.text[0:15]







class PostFile(models.Model):
    image = models.ImageField(upload_to="education/images")
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='images')
    def save( self, *args, **kwargs):
        super(PostFile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300 :
            output_size =(300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)