from django.contrib import admin
from .models import CustomUser, Course, Lesson, Quiz, Question, Choice, Enrollment,project

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_student', 'is_instructor')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_student', 'is_instructor')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'bio', 'profile_picture')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Roles', {'fields': ('is_student', 'is_instructor')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active', 'is_student', 'is_instructor'),
        }),
    )
    ordering = ('username',)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'instructor__username')
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'course__title')
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'course__title')
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz', 'order')
    search_fields = ('text', 'quiz__title')
    list_filter = ('quiz__title',)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')
    search_fields = ('text', 'question__text')
    list_filter = ('question__text', 'is_correct')

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_at')
    search_fields = ('student__username', 'course__title')
    list_filter = ('enrolled_at',)
    date_hierarchy = 'enrolled_at'

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(project)

# > python manage.py createsuperuser
# Username (leave blank to use 'prang'): admin
# Email address: admin@admin
# Email address: admin@gmail.com
# Password:1234Lisa@
# Password (again):1234Lisa@
# Superuser created successfully.