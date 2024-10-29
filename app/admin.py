from django.contrib import admin
from .models import User, Course, Content, Section, Enrollment, Review, Quiz, Question

# Register your models here.
admin.site.register(User)
admin.site.register(Content)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Enrollment)
admin.site.register(Review)
admin.site.register(Question)
admin.site.register(Quiz)
