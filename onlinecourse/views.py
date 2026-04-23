from django.shortcuts import render, redirect
from .models import Question, Choice, Submission

def submit(request):
    if request.method == 'POST':
        selected_choices = request.POST.getlist('choices')
        
        submission = Submission.objects.create()
        
        for choice_id in selected_choices:
            choice = Choice.objects.get(id=choice_id)
            submission.choices.add(choice)
        
        return redirect('show_exam_result')
    
    return redirect('home')


def show_exam_result(request):
    submissions = Submission.objects.all().last()
    selected_choices = submissions.choices.all()

    score = 0
    total = 0

    for choice in selected_choices:
        if choice.is_correct:
            score += 1
        total += 1

    context = {
        'score': score,
        'total': total,
    }

    return render(request, 'result.html', context)