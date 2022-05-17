from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from uiapp.forms import CommentForm
from uiapp.models import Comment


class HomeView(ListView):
    template_name = 'uiapp/home.html'
    model = Comment
    context_object_name = "lists"
    ordering = '-id'


def modal(request):
    form = CommentForm()
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
            html = "<div id='email-error' _='on load wait 1s trigger closeModal'>Success</div>"
            return HttpResponse(html, headers={'HX-Trigger': 'newList'})
        return HttpResponse('no')
    return render(request, 'uiapp/modal.html', {'form':form})


def check_comment(request):
    comment = request.POST.get('comment')
    comment_number = len(comment)
    if comment_number > 9:
        html = "<div id='modal_field' class='comment_error'>Count:<span id='comment-error'>The number of characters is the limit. %s</span></div>" % comment_number
        return HttpResponse(html)
    else:
        html = "<div id='modal_field'>Count:<span id='comment-error'>%s</span></div>" % comment_number
        return HttpResponse(html)


def list_comment(request):
    lists =  Comment.objects.all()

    context = {
        'lists':lists
    }

    return render(request, 'uiapp/comment-list.html', context)


def delete_comment(request, pk):

    list_item = get_object_or_404(Comment, pk=pk)

    if request.method == "POST":
        list_item.delete()
    lists = Comment.objects.all()

    context = {
        'lists':lists
    }

    return render(request, 'uiapp/comment-list.html', context)