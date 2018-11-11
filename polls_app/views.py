from django.shortcuts import render
from django.db.models import F  # F() makes db operations MUCH faster... Not
                                # required to load values into python memory, and prevents race
                                # conditions (2 people voting at same time, and only 1 gets counted).
from .models import Question
from blog_app.models import Post


# This first function uses .latest(). It's intended to be used on a home page,
# or some other higher traffic area.
def vote(request):
    question = Question.objects.latest('pub_date')
    if request.method == 'POST':
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
            selected_choice.votes = F('votes') + 1  # See imports in F for context
            selected_choice.save()
            request.session['you_voted'] = 'Voted'  # set a session value for global / home page vote
        except KeyError:
            pass
    return render(request, 'vote_results.html', {'question': question})


def blog_vote(request, year, month, day, post):
    post = Post.objects.get(publish__year=year, publish__month=month, publish__day=day, slug=post)
    question = post.question_set.first()   # Question.objects.latest('pub_date')
    if request.method == 'POST':
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
            selected_choice.votes = F('votes') + 1  # See imports in F for context
            selected_choice.save()
            request.session['you_voted{}'.format(post.pk)] = 'BlogVoted{}'.format(post.pk)  # Set a session value UNIQUE TO THIS POST
        except KeyError:
            pass
    return render(request, 'vote_results_blog.html', {'post': post, 'question': question})
