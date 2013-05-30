from django.http import HttpResponse
from django.forms.models import modelformset_factory
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.contrib.auth import authenticate, login
from album.models import Picture, Comment, PictureForm
from album.serializers import PictureSerializer, CommentSerializer, CommentAddSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.template import RequestContext

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders it's content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def index(request):
    if request.user.is_authenticated():
        ifadmin = True
    else:
        ifadmin = False
    # Do something for anonymous users.
    picture_list = Picture.objects.all()
    context = { 
            'picture_list' : picture_list,
            'ifadmin' : ifadmin, 
            }
    return render(request, 'album/index.html', context)

def detail(request, picture_id):
    if request.user.is_authenticated():
        ifadmin = True
    else:
        ifadmin = False
    context = { 
            'picture_id': picture_id,
            'ifadmin' : ifadmin, 
            }
    return render(request, 'album/detail.html', context)

def add(request):
    if not request.user.is_authenticated():
        return redirect('index')
    form = PictureForm() # A empty, unbound form
    # Render list page with the documents and the form
    return render_to_response('album/add.html',{'form': form}, context_instance=RequestContext(request))

@csrf_exempt
def picture_list(request):
    if request.method == 'GET':
        picture = Picture.objects.all()
        serializer = PictureSerializer(picture, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        if not request.user.is_authenticated():
            return redirect('index')
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to the document list after POST
            return redirect('index')
        else:
            return redirect('add')

@csrf_exempt
def picture_detail(request, pk):
    """
    Retrieve, update or delete a code picture.
    """
    picture = get_object_or_404(Picture, pk=pk)

    if request.method == 'GET':
        serializer = PictureSerializer(picture)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        if not request.user.is_authenticated():
            return redirect('index')
        data = JSONParser().parse(request)
        serializer = PictureSerializer(picture, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        if not request.user.is_authenticated():
            return redirect('index')
        picture.delete()
        return HttpResponse(status=204)




@csrf_exempt
def comment_list(request):
    if request.method == 'GET':
        if request.GET == {}:
            comments = Comment.objects.all()
        else:
            comments = Comment.objects.filter(picture=request.GET['pic_id'])
        serializer = CommentSerializer(comments, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        print(request.raw_post_data)
        data = JSONParser().parse(request)
        serializer = CommentAddSerializer(data=data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def comment_detail(request, pk):
    """
    Retrieve, update or delete a code comment.
    """
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        if not request.user.is_authenticated():
            return redirect('index')
        data = JSONParser().parse(request)
        serializer = CommentSerializer(comment, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        if not request.user.is_authenticated():
            return redirect('index')
        comment.delete()
        return HttpResponse(status=204)
