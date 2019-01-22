from django.http import JsonResponse
from book_watcha import recommend

def book(request):
    books = recommend.recommending_books(request.body.book_list, request.body.tag_list)
    data = {}

    return JsonResponse(data)
