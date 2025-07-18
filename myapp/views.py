from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageForm
from .models import Image

def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        form = ImageForm()
    else:
        form = ImageForm()

    img = Image.objects.all()
    return render(request, 'myapp/home.html', {'form': form, 'img': img})


#  ALLOW ANYONE TO DELETE
def delete_image(request, id):
    image = get_object_or_404(Image, id=id)
    image.delete()
    return redirect('home')
