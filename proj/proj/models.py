from django.db import models

class tan90_user(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    admin = models.BooleanField()
    mail = models.EmailField()
    phone = models.CharField(max_length=20)
    department = models.ForeignKey('tan90_department', on_delete=models.CASCADE)
    face = models.ImageField(upload_to='img')
    introduce = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)

class tan90_user_course(models.Model):
    user = models.ForeignKey('tan90_user', on_delete=models.CASCADE)
    position = models.ForeignKey('tan90_chapter', on_delete=models.CASCADE)
    index = models.SmallIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    finished = models.BooleanField()

class tan90_department(models.Model):
    name = models.CharField(max_length=50)

class tan90_user_logs(models.Model):
    user = models.ForeignKey('tan90_user', on_delete=models.CASCADE)
    course = models.ForeignKey('tan90_course', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class tan90_course(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey('tan90_category', on_delete=models.CASCADE)
    timedelta = models.IntegerField()
    department = models.ManyToManyField('tan90_department')
    introduce = models.CharField(max_length=50)

class tan90_category(models.Model):
    name = models.CharField(max_length=20)

class tan90_chapter(models.Model):
    name = models.CharField(max_length=20)
    index = models.SmallIntegerField()
    course = models.ForeignKey('tan90_course', on_delete=models.CASCADE)

class tan90_video(models.Model):
    chapter = models.ForeignKey('tan90_course', on_delete=models.CASCADE)
    index = models.SmallIntegerField()
    video = models.FileField(upload_to='video')
    timedelta = models.IntegerField()
    name = models.CharField(max_length=20)

class tan90_pdf(models.Model):
    chapter = models.ForeignKey('tan90_chapter', on_delete=models.CASCADE)
    index = models.SmallIntegerField()
    pdf = models.FileField(upload_to='pdf')
    timedelta = models.IntegerField()
    name = models.CharField(max_length=20)

class tan90_discussion(models.Model):
    chapter = models.ForeignKey('tan90_chapter', on_delete=models.CASCADE)
    user = models.ForeignKey('tan90_user', on_delete=models.CASCADE)
    time = models.DateTimeField()
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=140)

class tan90_response(models.Model):
    discussion = models.ForeignKey('tan90_discussion', on_delete=models.CASCADE)
    user = models.ForeignKey('tan90_user', on_delete=models.CASCADE)
    time = models.DateTimeField()
    content = models.CharField(max_length=140)

class tan90_problem(models.Model):
    type = models.SmallIntegerField()
    index = models.SmallIntegerField()
    content = models.CharField(max_length=512)
    exam = models.ForeignKey('tan90_exam', on_delete=models.CASCADE)

class tan90_exam(models.Model):
    chapter = models.ForeignKey('tan90_chapter', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    end_time = models.DateTimeField()
    score = models.SmallIntegerField()

class tan90_user_exam(models.Model):
    exam = models.OneToOneField('tan90_exam', on_delete=models.CASCADE)
    user = models.ForeignKey('tan90_user', on_delete=models.CASCADE)
    score = models.SmallIntegerField()
    time = models.DateTimeField()

class tan90_error_problem(models.Model):
    user = models.ForeignKey('tan90_user', on_delete=models.CASCADE)
    problem = models.ForeignKey('tan90_problem', on_delete=models.CASCADE)

class tan90_notice(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=512)
    poster = models.ForeignKey('tan90_user', on_delete=models.CASCADE)

class tan90_face(models.Model):
    face = models.ImageField(upload_to='face')
    user = models.OneToOneField('tan90_user')

class tan90_cover(models.Model):
    cover = models.ImageField(upload_to='cover')
    course = models.ForeignKey('tan90_course', on_delete=models.CASCADE)

