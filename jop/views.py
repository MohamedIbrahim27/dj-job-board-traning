from multiprocessing import context
from django.shortcuts import render
from .models import jop
from django.core.paginator import Paginator
from .form import ApplyForm
from django.views.generic import ListView,DetailView
# Create your views here.

def jop_list(request):
    jop_list= jop.objects.all()
    
    paginator = Paginator(jop_list, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    
    context={'jops' :page_obj}
    return render(request, 'jop/jop_list.html', context)


def jop_detail(request ,slug):
    jop_detail = jop.objects.get(slug=slug)
    
    if request.method=='POST':
        form=ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.jop= jop_detail
            myform.save()
    
    else:
        form = ApplyForm()
    
    context= {'jop' :jop_detail , 'form':form}
    return render(request , 'jop/jop_detail.html', context)

class JopList(ListView):
    model= jop
    
class JopDetail(DetailView):
    model= jop