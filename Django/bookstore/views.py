from django.shortcuts import render
from bookstore.models import Book
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
# noinspection PyTypeChecker
# def retrieveBooks(request):
#     books = Book.objects.values("title", "pub", "price", "market_price")
#     for i, data in books:
#         name = data[i].get("title")
#         public = data[i].get("pub")
#         price = data[i].get("price")
#         market_price = data[i]['market_price']
#         HttpResponse(name, public, price, market_price)
def retrieveBooks(request):
    books = Book.objects.values("title", "pub", "price", "market_price")
    response_content = ""
    for data in books:
        name = data.get("title")
        public = data.get("pub")
        price = data.get("price")
        market_price = data['market_price']
        response_content += f"Name: {name}, Public: {public}, Price: {price}, Market Price: "f"{market_price}\n"
    return HttpResponse(response_content)


def all_book(request):
    # all_books = Book.objects.all()
    all_books = Book.objects.filter(is_activate=True)
    return render(request, "bookstore/all_book.html", locals())


# noinspection PyBroadException
def update_book(request, book_id):
    # bookstore/update_book/1
    try:
        book = Book.objects.get(id=book_id)
        HttpResponse(f"Book with ID {book_id} has been updated.")
    except Exception as e:
        print('Update book error is %s' % e)
        return HttpResponse('--The book is not existed')

    if request.method == 'GET':
        return render(request, "bookstore/update_book.html", locals())
    elif request.method == "POST":
        price = request.POST['price']
        market_price = request.POST['market_price']

        book.price = price
        book.market_price = market_price
        book.save()
        return HttpResponseRedirect('/bookstore/all_book')


def delete_book(request):
    book_id = request.GET.get('book_id')
    if not book_id:
        return HttpResponse("REQUEST ERROR")
    try:
        book = Book.objects.get(id=book_id, is_activate=True)
    except Exception as e:
        print('Delete book error is %s' % e)
        return HttpResponse('--The book is not existed')

    book.is_activate = False
    book.save()

    return HttpResponseRedirect('/bookstore/all_book')
