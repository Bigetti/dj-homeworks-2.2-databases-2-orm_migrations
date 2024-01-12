from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):

    template = 'school/students_list.html'

    # Получаем все объекты студентов
    students = Student.objects.all()

    # Передаем студентов в контекст представления
    context = {'students': students}

    print("students_list view is called!")

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
