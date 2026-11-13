# from django.http import HttpResponse, Http404
#
# PRODUCTS = [
#     {"id": 1, "name": "Laptop", "price": 1800},
#     {"id": 2, "name": "Headphones", "price": 150},
#     {"id": 3, "name": "Mouse", "price": 40},
# ]
#
# def home(request):
#     return HttpResponse("<h1>myshop</h1><a href='/products/'>products</a>")
#
# def about(request):
#     return HttpResponse("<h1>about</h1><p>me var giorgi!</p>")
#
# def product_list(request):
#     html = "<h1>products</h1><ul>"
#     for p in PRODUCTS:
#         html=html+"<li><a href='/products/"+str(p["id"])+"/'>"
#         html=html+p["name"]+":"+str(p["price"])+" ₾</a></li>"
#     html=html+"</ul>"
#     return HttpResponse(html)
# def product_detail(request, pk):
#     for p in PRODUCTS:
#         if p["id"] == pk:
#             return HttpResponse("<h1>" + p["name"] + "</h1><p>" + str(p["price"]) + " ₾</p>")
#     raise Http404("Product not found")