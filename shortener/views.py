from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Url

@csrf_exempt
def create_short_url(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            original_url = data.get('original_url')
            
            if not original_url:
                return JsonResponse({'error': 'original_url gerekli'}, status=400)

            
            url_obj, created = Url.objects.get_or_create(original_url=original_url)
            
            
            host = request.get_host() 
            short_url = f"http://{host}/{url_obj.short_code}"
            
            return JsonResponse({
                'original_url': url_obj.original_url,
                'short_url': short_url,
                'short_code': url_obj.short_code,
                'is_new': created
            }, status=201)
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Geçersiz JSON formatı'}, status=400)

def redirect_url(request, short_code):
    url_obj = get_object_or_404(Url, short_code=short_code)
    
    url_obj.click_count += 1
    url_obj.save()
    
    return HttpResponseRedirect(url_obj.original_url)

def get_analytics(request, short_code):
    if request.method == 'GET':
        url_obj = get_object_or_404(Url, short_code=short_code)
        return JsonResponse({
            'original_url': url_obj.original_url,
            'short_code': url_obj.short_code,
            'click_count': url_obj.click_count,
            'created_at': url_obj.created_at
        })