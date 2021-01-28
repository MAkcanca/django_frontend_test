from django.template.response import TemplateResponse
from core.models import BlogPost
 
def index(request):
    all_posts = BlogPost.objects.all().order_by('-date')
    template_data = {'posts' : all_posts[:3]}
 
    return TemplateResponse(request, 'core/index.html', template_data)
