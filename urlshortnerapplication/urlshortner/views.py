from django.shortcuts import render,redirect

# Create your views here.
from .models import URL
# myapp/views.py
from django.shortcuts import render
from .models import URL

def home_page(request):
    context = {}
    if request.method == 'POST':
        # Get the URL from the form submission
        original_link = request.POST.get('url')

        # Create and save a new instance of the URL model
        new_url = URL.objects.create(original_link=original_link)
        
        # Pass the newly created URL's uuid to the context for displaying
        context['uuid'] = new_url.uuid
        context['url'] = original_link

    return render(request, 'Home.html', context=context)



def go_to_newURl(request, shortID):
    try:
        # Fetch URL details by shortID (UUID)
        url_details = URL.objects.get(uuid=shortID)

        # Redirect to the original link if it exists
        return redirect(url_details.original_link)
    
    except URL.DoesNotExist:
        # Handle the case where the shortID does not exist
        return render(request, 'not_found.html', status=404)
    
    except Exception as e:
        # Optionally handle other exceptions (like URL-related issues)
        return render(request, 'not_found.html', status=404)
