from django.http import HttpResponse, Http404

RECIPES = [
    {"id": 1, "slug": "khinkali", "name": "ხინკალი", "category": "main",
     "minutes": 90, "vegetarian": False,
     "ingredients": ["ფქვილი", "საქონლის ხორცი", "ღორის ხორცი",
                     "ხახვი", "კვლიავი"]},
    {"id": 2, "slug": "khachapuri", "name": "ხაჭაპური", "category": "bakery",
     "minutes": 60, "vegetarian": True,
     "ingredients": ["ფქვილი", "იმერული ყველი", "კვერცხი", "კარაქი"]},
    {"id": 3, "slug": "lobiani", "name": "ლობიანი", "category": "bakery",
     "minutes": 75, "vegetarian": True,
     "ingredients": ["ფქვილი", "ლობიო", "ხახვი", "კარაქი"]},
    {"id": 4, "slug": "pkhali", "name": "ფხალი", "category": "snack",
     "minutes": 30, "vegetarian": True,
     "ingredients": ["ისპანახი", "ნიგოზი", "ნიორი", "ქინძი"]},
    {"id": 5, "slug": "churchkhela", "name": "ჩურჩხელა", "category": "dessert",
     "minutes": 240, "vegetarian": True,
     "ingredients": ["ნიგოზი", "ყურძნის წვენი", "ფქვილი"]},
    {"id": 6, "slug": "chakapuli", "name": "ჩაქაფული", "category": "main",
     "minutes": 120, "vegetarian": False,
     "ingredients": ["ცხვრის ხორცი", "ტყემალი", "ტარხუნა", "თეთრი ღვინო"]},
]


def page(title, body):
    """ყველა გვერდისთვის ერთნაირი HTML ჩარჩო."""
    return HttpResponse(
        f"<h1>{title}</h1>{body}<hr>"
        f"<a href='/recipes/'>← ყველა რეცეპტი</a>"
    )


def find_recipe(pk):
    for r in RECIPES:
        if r["id"] == pk:
            return r
    return None


def recipe_list(request):
    results = RECIPES

    category = request.GET.get("category")
    max_time = request.GET.get("max_time")
    vegetarian = request.GET.get("vegetarian")

    if category:
        results = [r for r in results if r["category"] == category]
    if max_time:
        results = [r for r in results if r["minutes"] <= int(max_time)]
    if vegetarian == "yes":
        results = [r for r in results if r["vegetarian"]]

    if not results:
        return page("რეცეპტები", "<ul></ul><p>ვერაფერი მოიძებნა</p>")

    items = "".join(
        f"<li><a href='/recipes/{r['id']}/'>{r['name']}</a> · {r['minutes']} წთ</li>"
        for r in results
    )
    return page("რეცეპტები", f"<ul>{items}</ul>")


def recipe_detail(request, pk):
    r = find_recipe(pk)
    if r is None:
        raise Http404("რეცეპტი ვერ მოიძებნა")

    veg = "კი" if r["vegetarian"] else "არა"
    ingredients = "".join(f"<li>{i}</li>" for i in r["ingredients"])
    body = (
        f"<p>მომზადების დრო: {r['minutes']} წთ</p>"
        f"<p>კატეგორია: {r['category']}</p>"
        f"<p>ვეგეტარიანული: {veg}</p>"
        f"<ul>{ingredients}</ul>"
    )
    return page(r["name"], body)


def category_detail(request, name):
    results = [r for r in RECIPES if r["category"] == name]
    if not results:
        raise Http404("კატეგორია ვერ მოიძებნა")

    items = "".join(
        f"<li><a href='/recipes/{r['id']}/'>{r['name']}</a> · {r['minutes']} წთ</li>"
        for r in results
    )
    return page(name, f"<ul>{items}</ul>")
