from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Enrollment, Question, Choice, Submission

def submit(request, course_id):
    if request.method == 'POST':
        
        course = get_object_or_404(Course, pk=course_id)
        enrollment = get_object_or_404(Enrollment, user=request.user, course=course)

        submission = Submission.objects.create()

        choices = request.POST.getlist('choice')

        for choice_id in choices:
            choice = Choice.objects.get(id=choice_id)
            submission.choices.add(choice)

        submission.save()

        return redirect('show_exam_result', course_id=course.id, submission_id=submission.id)


def show_exam_result(request, course_id, submission_id):
    
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)

    selected_choices = submission.choices.all()
    selected_ids = [choice.id for choice in selected_choices]

    total_score = 0
    possible_score = 0

    questions = Question.objects.filter(lesson__course=course)

    for question in questions:
        possible_score += 1
        correct_choices = question.choice_set.filter(is_correct=True)
        selected_for_question = selected_choices.filter(question=question)

        if set(correct_choices) == set(selected_for_question):
            total_score += 1

    context = {
        'course': course,
        'selected_ids': selected_ids,
        'grade': total_score,
        'possible': possible_score,
    }

    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)