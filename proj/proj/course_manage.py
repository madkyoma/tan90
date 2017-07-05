from django.http import HttpResponse
from django.core.paginator import Paginator
from . import models
import json


def get_category(request):
    try:
        cat = models.tan90_category.objects.all()
        limit = request.POST.get('limit', 20)
        page_index = request.POST.get('page', 1)
        p = Paginator(cat, limit)
        res = []
        try:
            res = list(p.page(page_index).object_list)
        except BaseException as e:
            print(e)
        return HttpResponse(json.dumps(
            {'code': '1000', 'msg': 'ok', 'category': res, 'page_cnt': p.count},
            ensure_ascii=False)
        )
    except BaseException as e:
        print(e)
        return HttpResponse(json.dumps({'code': '4000', 'msg': 'serve error'}))


def add_category(request):
    try:
        user_id = request.session.get('id')
        if not user_id:
            return HttpResponse(json.dumps({'code': '1001', 'msg': 'not login'}))

        user = models.tan90_user.objects.get(id=int(user_id))
        if not user.admin:
            return HttpResponse(json.dumps({'code': '1002', 'msg': 'not admin'}))

        category_name = request.POST.get('category_name')
        models.tan90_category.objects.get_or_create(name=category_name)
        return HttpResponse(json.dumps({'code': '1000', 'msg': 'ok'}))

    except BaseException as e:
        print(e)
        return HttpResponse(json.dumps({'code': '4000', 'msg': 'serve error'}))


def del_category(request):
    try:
        user_id = request.session.get('id')
        if not user_id:
            return HttpResponse(json.dumps({'code': '1001', 'msg': 'not login'}))

        user = models.tan90_user.objects.get(id=int(user_id))
        if not user.admin:
            return HttpResponse(json.dumps({'code': '1002', 'msg': 'not admin'}))

        category_name = request.POST.get('category_name')
        category = models.tan90_category.objects.get(name=category_name)
        relate_course = models.tan90_course.objects.filter(department__tan90_course__category=category)
        if relate_course:
            return HttpResponse(json.dumps({'code': '1003', 'msg': 'related course exist'}))

        category.delete()
        return HttpResponse(json.dumps({'code': '1000', 'msg': 'ok'}))
    except BaseException as e:
        print(e)
        return HttpResponse(json.dumps({'code': '4000', 'msg': 'serve error'}))


def add_course(request):
    try:
        user_id = request.session.get('id')
        if not user_id:
            return HttpResponse(json.dumps({'code': '1001', 'msg': 'not login'}))
        user = models.tan90_user.objects.get(id=int(user_id))
        if not user.admin:
            return HttpResponse(json.dumps({'code': '1002', 'msg': 'not admin'}))

        tmp_course = models.tan90_course()
        course_name = request.POST.get('course_name')
        department_names = request.POST.getlist('department_names')
        category_name = request.POST.get('category_name')
        introduce = request.POST.get('introduce')
        if not introduce:
            introduce = 'A simple course'

        test_course = models.tan90_course.objects.filter(name=course_name)
        if test_course:
            return HttpResponse(json.dumps({'code': '1003', 'msg': 'same course exist'}))

        category = models.tan90_category.objects.get(name=category_name)

        if not department_names:
            tmp_course.department.add(models.tan90_department.objects.all())
        else:
            tmp_course.department.add(models.tan90_department.objects.filter(name__in=department_names))
        tmp_course.name = course_name
        tmp_course.category = category
        tmp_course.timedelta = 0
        tmp_course.introduce = introduce
        tmp_course.save()
        return HttpResponse(json.dumps({'code': '1000', 'msg': 'ok'}))
    except BaseException as e:
        print(e)
        return HttpResponse(json.dumps({'code': '4000', 'msg': 'serve error'}))


def del_course(request):
    try:
        user_id = request.session.get('id')
        if not user_id:
            return HttpResponse(json.dumps({'code': '1001', 'msg': 'not login'}))
        user = models.tan90_user.objects.get(id=user_id)
        if not user.admin:
            return HttpResponse(json.dumps({'code': '1002', 'msg': 'not admin'}))

        course_name = request.POST.get('course_name')

        try:
            course = models.tan90_course.objects.get(name=course_name)
            course.delete()
        except BaseException as e:
            return HttpResponse(json.dumps({'code': '1001', 'msg': 'not find such course'}))
        return HttpResponse(json.dumps({'code': '1000', 'msg': 'ok'}))

    except BaseException as e:
        print(e)
        return HttpResponse(json.dumps({'code': '4000', 'msg': 'serve error'}))


def add_video(request):
    pass


def add_pdf(request):
    pass
