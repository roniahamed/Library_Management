
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Book, Wishlist, Borrowing
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class Book_list(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'book_list'


class Book_details(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book_detail'
    pk_url_kwarg = 'id'


class Book_search(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        query = self.request.GET.get('keyword')
        if query:
            object_list = self.model.objects.filter(
                Q(title__icontains=query) | Q(author__icontains=query) | Q(ISBN__icontains=query) | Q(genre__icontains=query))
        else:
            object_list = self.model.objects.none()
        return object_list


class wishlist_show(ListView):
    model = Wishlist
    template_name = 'wishlist_list.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)


@login_required
def add_wishlist(request, pk):
    if request.user.is_authenticated:
        wishlist_item = Wishlist.objects.filter(user=request.user, book=pk)
        if wishlist_item:
            messages.success(request, 'All ready add to wishlist')
        else:
            product = Book.objects.get(id=pk)
            wishlist_item = Wishlist(user=request.user, book=product)
            wishlist_item.save()
            messages.success(request, 'successfully Add to Wishlist')
    else:
        messages.success(request, 'You is Not a Authenticated User')
        redirect('login')
    context = Book.objects.get(id=pk)
    return render(request, 'book_detail.html', {'book_detail': context})


@login_required
def remove_wishlist(request, pk):
    messages.success(request, 'successfully delate to Wishlist')
    wishlist = get_object_or_404(Wishlist, user=request.user, id=pk)
    wishlist.delete()
    return redirect('wishlist')


def Borrow_Book_list(request):
    if request.user.is_authenticated:
        context = Borrowing.objects.filter(user=request.user)
    else:
        messages.warning(
            request, "You is not Authenticated User Please Login Now")
        return redirect('login')
    return render(request, 'borrow.html', {'book_list': context})


def borrowing(request, pk):
    context = Book.objects.get(id=pk)
    if request.user.is_authenticated:
        if request.method == "POST":
            borrow_item = Borrowing.objects.filter(book=pk, user=request.user)
            return_date = request.POST['return_date']
            if borrow_item:
                messages.success(request, 'All ready add to Borrowing')
                return redirect('borrow_book_list')
            elif context.availability == 0:
                messages.success(request, 'This Book Out of Stock')
            else:
                
                book = Book.objects.get(id=pk)
                book.availability = book.availability - 1
                book.save()
                borrow = Borrowing(
                    book=book, user=request.user, due_date=return_date)
                borrow.save()
                messages.success(request, 'This book Borrowing Success')
                return redirect('borrow_book_list')
    else:
        messages.warning(
            request, "You is not Authenticated User Please Login Now")
        return redirect('login')
    context = Book.objects.get(id=pk)
    return render(request, 'book_detail.html', {'book_detail': context})


def borrowing_return(request,pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            borrow_list = Borrowing.objects.get(user=request.user,id=pk)
            books = Book.objects.get(id=borrow_list.book.id)
            books.availability += 1
            books.save()
            borrow_list.delete()
            messages.success(request,f"'{books.title}' This Book Return is Successful")
            return redirect('borrow_book_list')
    else:
        messages.warning(request,"You is't Authenticated User!")
        return redirect("login")
    

def add_book(request):
    if request.user.is_superuser:
        if request.method == "POST":
            title = request.POST['title']
            author = request.POST['author']
            isbn = request.POST['ISBN']
            genre = request.POST['genre']
            availability = request.POST['availability']
            book = Book(title=title,author=author,ISBN=isbn,genre=genre,availability=availability)
            book.save()
            return redirect('/')
        return render(request,'add_book.html')
    elif request.user.is_authenticated:
        messages.warning(request,"You does't Admin!")
        return redirect("/")
    else:
        messages.warning(request,"You does't Admin!")
        return redirect("login")



def edit_book(request,pk):
    if request.user.is_superuser:
        content = Book.objects.get(id=pk)
        if request.method == "POST":
            content.title = request.POST['title']
            content.author = request.POST['author']
            content.isbn = request.POST['ISBN']
            content.genre = request.POST['genre']
            content.availability = request.POST['availability']
            content.save()
            return redirect('/')
        return render(request,'add_book.html',{'book':content})
    elif request.user.is_authenticated:
        messages.warning(request,"You does't Admin!")
        return redirect("/")
    else:
        messages.warning(request,"You does't Admin!")
        return redirect("login")



def Book_Delete(request,pk):
    if request.user.is_superuser:
        book = Book.objects.get(id=pk)
        messages.success(request,"Book is Delete Successful")
        book.delete()
        return redirect('/')
    elif request.user.is_authenticated:
        messages.warning(request,"You does't Admin!")
        return redirect("/")
    else:
        messages.warning(request,"You does't Admin!")
        return redirect("login")
    
        
