from django.shortcuts import render, get_object_or_404, redirect
from tutorial.models import *
from django.http import HttpResponse


def index(request):
    content = {'nav': 'tutorial',
               'title': 'Vaping.com | Tutorial',
               'tutorials': Tutorial.objects.all()}

    return render(request, 'tutorial/index.html', context=content)


def tutorial_detail(request, pk):

    tutorial = get_object_or_404(Tutorial, pk=pk)

    author = TutorialComments.objects.filter(replay_to=None, tutorial__id=pk).order_by('-created_at')
    lista_author = []
    for author_row in author:
        son = TutorialComments.objects.filter(replay_to=author_row, tutorial__id=pk)
        lista_son = []
        for son_row in son:
            granson = TutorialComments.objects.filter(replay_to=son_row, tutorial__id=pk)
            lista_granson = []

            for granson_row in granson:
                granson_dict = {
                    'id': granson_row.pk,
                    'comment': granson_row.comment,
                    'user': granson_row.user,
                    'date': granson_row.created_at,
                    'liked': granson_row.liked,
                    'avatar': granson_row.user.profile_pic.url,
                    'level': 3
                }
                lista_granson.append(granson_dict)

            son_dict = {   'id': son_row.pk,
                            'comment': son_row.comment,
                            'user': son_row.user,
                            'date': son_row.created_at,
                            'liked': son_row.liked,
                            'level': 2,
                            'avatar': son_row.user.profile_pic.url,
                            'chield': lista_granson}

            lista_son.append(son_dict)

        author_dict = {   'id': author_row.pk,
                            'comment': author_row.comment,
                            'user': author_row.user,
                            'date': author_row.created_at,
                            'liked': author_row.liked,
                            'avatar': author_row.user.profile_pic.url,
                            'level': 1,
                            'chield': lista_son}

        lista_author.append(author_dict)

    if request.user.is_authenticated:
        user_pic = UserProfileInfo.objects.get(user=request.user).profile_pic.url
    else:
        user_pic = ''

    content = {'nav': 'recipe',
               'title': 'Vaping.com | Recipes Detail',
               'comments' : lista_author,
               'avatar': user_pic,
               'tutorial' : tutorial,
     }
    return render(request, 'tutorial/{}.html'.format(tutorial.page), context=content)


def comment(request):

    post = request.POST
    print(post)

    if post['comment'] != '':

        comment = TutorialComments()
        comment.tutorial_id = int(post['tutorial'])
        comment.replay_to_id = post['reply_to']
        comment.user_id = int(post['user'])
        comment.comment = post['comment']
        comment.save()


    return redirect('tutorial:tutorial_detail', pk=post['tutorial'])