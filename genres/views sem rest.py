import json
from django.http import JsonResponse
from genres.models import Genre
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def genre_create_list_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = [{'id': genre.id, 'name': genre.name} for genre in genres]
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name=data['name'])
        new_genre.save()
        return JsonResponse({'id': new_genre.id, 'name': new_genre.name}, status=201)
    
@csrf_exempt   
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'GET':
        data = {'id': genre.id, 'name': genre.name}
        return JsonResponse(data, safe=False)
    elif request.method == "PUT":
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()
        return JsonResponse({'id': genre.id, 'name': genre.name}, status=201)
    elif request.method == "DELETE":
        genre.delete()
        return JsonResponse({'message': 'Deleted successfully'}, status=204)