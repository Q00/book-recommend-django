
from django.http import HttpResponse 
from .book_watcha import recommend
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def book(request):
    print(request.method)
    if request.method == 'POST':
        index= 0
        book_list = []
        tag_list = []
        book_flag = True
        tag_flag = True
        while(True):
            print('while')
            if book_flag:
                try:
                    book_data = request.POST.get("book_list[books]["+index+"]")
                    book_list.append(book_data)
                except:
                    book_flag = False
            if tag_flag:
                try:
                    tag_data= request.POST.get("tag_list[tags]["+index+"]")
                    tag_list.append(tag_data)
                except:
                    tag_flag = False
            if book_flag == False and tag_flag == False:
                break

        books = recommend.recommending_books(book_list, tag_list)
        print(books)    
        data = json.dumps(books, ensure_ascii=False)
        print(data)
        return HttpResponse(data, content_type='application/json; charset=utf-8')
