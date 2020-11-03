from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Category_Name, Document, User
from .forms import DocumentForm
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy


def index(request):
    data = Document.objects.all()
    data2 = Category_Name.objects.all()
    return render(request, 'index.html', {
        'data': data,
        "data2": data2
    })


def login(request):
    data2 = Category_Name.objects.all()
    if request.method == "POST":
        get_email = request.POST['email']
        get_password = request.POST['password']

        data = User.objects.get(email=get_email)
        db_password = data.password
        if get_password == db_password:
            request.session['authenticate'] = True
            request.session['email'] = get_email
            request.session['username'] = data.fname + " " + data.lname
            request.session['id'] = data.id
            return redirect('/dashboard')
    return render(request, 'login.html', {'data2': data2})


def dashboard(request):
    if request.session.has_key('authenticate'):
        if request.session['authenticate']:
            return render(request, 'dashboard.html', {
                'username': request.session['username']
            })
        else:
            return redirect('/')
    return render(request, 'dashboard.html')


def logout(request):
    if request.session['authenticate']:
        request.session['authenticate'] = False
        request.session['email'] = ""
        request.session['username'] = ""
        del request.session['id']
    return redirect("/")


def details(request, pk):
    data = get_object_or_404(Document, pk=pk)
    data2 = Category_Name.objects.all()
    return render(request, 'detail.html', {'data': data, 'data2': data2})


def create_post(request):
    if request.session['authenticate']:
        form = DocumentForm()
        images = ['jpg', 'jpeg', 'png']
        pdf = ['pdf']
        if request.method == 'POST':
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                album = form.save(commit=False)
                album.document = request.FILES['document']
                file_type = album.document.url.split('.')[-1].lower()
                if file_type not in pdf:
                    return render(request, 'create123.html')
                album.image = request.FILES['image']
                image_type = album.image.url.split('.')[-1].lower()
                if image_type not in images:
                    return render(request, 'create786.html')
                album.save()
                pk = album.id
                return redirect('/' + str(pk))
            return render(request, 'create.html', {'form': form})
        else:
            return render(request, 'create.html', {'form': form})
    return redirect("/")


class Updatecategory(UpdateView):
    model = Document
    fields = ["title", "description", "document", "category", "author", "image"]
    template_name = 'create.html'

    def form_valid(self, form):
        if self.request.session['authenticate']:
            user = form.save(commit=True)
            user.save()
            return HttpResponseRedirect(self.get_success_url())
        return redirect("/")


class Deletecategory(DeleteView):
    model = Document
    success_url = reverse_lazy("index")


def mybooks(request, pk):
    my_books = Document.objects.filter(category_id=pk)
    data2 = Category_Name.objects.all()
    cat =  Category_Name.objects.filter(Category_id = pk)
    return render(request, 'mypost.html', {'data': my_books, 'data2': data2, 'cat': cat[0].Category_name})


def allbooks(request):
    data = Document.objects.all()
    return render(request, "allbooks.html", {'data': data})


def allcategories(request):
    category_data = Category_Name.objects.all()
    return render(request, "allcategories.html", {'category_data': category_data})


