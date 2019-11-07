from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from login.models import UserProfileInfo
from .models import *


class Index(generic.ListView):
    model = Recipes
    template_name = 'recipe/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context = { 'recipes' : Recipes.objects.all(),
                      'nav' : 'recipe',
                      'title' : 'Vaping.com | Recipes'}
        return context


def RecipeDetailView(request, pk):

    author = RecipeComments.objects.filter(replay_to=None, recipe__id=pk).order_by('-created_at')
    lista_author = []
    for author_row in author:
        son = RecipeComments.objects.filter(replay_to=author_row, recipe__id=pk)
        lista_son = []
        for son_row in son:
            granson = RecipeComments.objects.filter(replay_to=son_row, recipe__id=pk)
            lista_granson = []

            for granson_row in granson:
                granson_dict = {
                    'id': granson_row.pk,
                    'comment': granson_row.comment,
                    'user': granson_row.user.username,
                    'date': granson_row.created_at,
                    'liked': granson_row.liked,
                    'avatar': UserProfileInfo.objects.get(user__id=granson_row.user.pk).profile_pic.url,
                    'level': 3
                }
                lista_granson.append(granson_dict)

            son_dict = {   'id': son_row.pk,
                            'comment': son_row.comment,
                            'user': son_row.user.username,
                            'date': son_row.created_at,
                            'liked': son_row.liked,
                            'level': 2,
                            'avatar': UserProfileInfo.objects.get(user__id=son_row.user.pk).profile_pic.url,
                            'chield': lista_granson}

            lista_son.append(son_dict)

        author_dict = {   'id': author_row.pk,
                            'comment': author_row.comment,
                            'user': author_row.user.username,
                            'date': author_row.created_at,
                            'liked': author_row.liked,
                            'avatar': UserProfileInfo.objects.get(user__id=author_row.user.pk).profile_pic.url,
                            'level': 1,
                            'chield': lista_son}

        lista_author.append(author_dict)

    recipe = get_object_or_404(Recipes, pk=pk)

    flavour = Flavour.objects.filter(recipe__id=pk)
    flavour_quant = 0
    for f in flavour:
        flavour_quant += f.quant

    if request.user.is_authenticated:
        user_pic = UserProfileInfo.objects.get(user=request.user).profile_pic.url
    else:
        user_pic = ''
    content = {'recipe': recipe,
               'flavor_quant': flavour_quant,
                'nav': 'recipe',
               'title': 'Vaping.com | Recipes Detail',
               'comments' : lista_author,
               'avatar': user_pic,
               'flavours': flavour}
    return render(request, 'recipe/recipe-detail.html', context=content)


def comment(request):

    post = request.POST
    print(post)
    if post['comment'] != '':
        try:
            comment = RecipeComments()
            comment.recipe_id = int(post['recipe'])
            comment.replay_to_id = post['reply_to']
            comment.user_id = int(post['user'])
            comment.comment = post['comment']
            comment.save()
        except Exception as e:
            return HttpResponse('Error occurred, Please go back and try again')

    return redirect('recipe:recipe-detail', pk=post['recipe'])