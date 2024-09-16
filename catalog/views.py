from django.shortcuts import render
from .models import Book, BookInstance, Author
from django.views import generic

#this is for authorizing views for only logged in people
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    # Number of visits to shi view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context=context)

class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book

class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author

class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book

class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author
