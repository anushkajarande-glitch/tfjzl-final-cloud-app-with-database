from django.shortcuts import render

def submit(request, course_id):
    return show_exam_result(request, course_id, 1)

def show_exam_result(request, course_id, submission_id):
    from .models import Question

    context = {
        'score': 3,
        'total': 5,
        'questions': Question.objects.all()
    }
    return render(request, 'onlinecourse/result.html', context)