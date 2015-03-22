from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from chat.forms import CommentForm
from chat.models import Comment


class IndexView(TemplateView):
    template_name = 'chat/chatroom.html'

    def post(self, request, *args, **kwargs):
        request.session['name'] = request.POST['name']
        return redirect('/chat/chat/')

class ChatView(TemplateView):

    def get(self, request, *args, **kwargs):
        if request.session.get('name'):
            comments = Comment.objects.all()
            dic = {
                'name': request.session['name'],
                'form': CommentForm,
                'comments': comments
            }
            return render(request, 'chat/chat.html', dic)
        else:
            return redirect('/chat/chatroom')

    def post(self, request, *args, **kwargs):
        Comment.objects.create(
            user = request.session['name'],
            comment = request.POST['comment']
        )
        return redirect('/chat/chat/')

@csrf_exempt
def create_comment(request):
    Comment.objects.create(
        user = request.POST['user'],
        comment = request.POST['comment']
    )
    response = JsonResponse({'user': request.POST['user'], 'comment': request.POST['comment']})
    return HttpResponse(response.content)