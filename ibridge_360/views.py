from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, 'home.html')

def show_data(request):
    query = request.GET.get('q')  # 'q' matches the input's name attribute
    print('Searched ID: ', query)

    last_data = []
    if query:
        last_data = UserActivity.objects.filter(user_id=query).order_by('-id')

    else:
        last_data = UserActivity.objects.all().order_by('-id')
    
    print('final data: ', last_data)

     # Pagination logic
    page_number = request.GET.get('page')  # Get the page number from GET parameters
    paginator = Paginator(last_data, 10)  # Show 10 records per page

    try:
        page_obj = paginator.get_page(page_number)
    except Exception as e:
        print(f"Error: {e}")
        page_obj = paginator.get_page(1)  # If an error occurs, default to the first page


    return render(request, 'datapage.html', {"records": page_obj})