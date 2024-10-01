from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def list_books(request):
    books = [
        {'title': 'Django 3 Web Development CookBook Fourth Edition', 'author': 'Aidas Bendoraitis', 'rating': 3250},
        {'title': 'Two Scoops of Django 3.x', 'author': 'Daniel Feldroy', 'rating': 1570},
        {'title': 'Django for Professionals', 'author': 'William S. Vincent', 'rating': 2100},
        {'title': 'Django for APIs', 'author': 'William S. Vincent', 'rating': 2540}
    ]
    return render(request, 'listbook.html', {'books': books})
