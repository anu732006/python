from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY="123",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
    MIDDLEWARE=[]
)

import django
django.setup()

from django.http import HttpResponse
from django.urls import path

products = []


def home(request):
    html = """
    <h1>Product Management</h1>

    <form method="post" action="/add/">
        Product Name:
        <input name="name"><br><br>

        Price:
        <input name="price"><br><br>

        Quantity:
        <input name="quantity"><br><br>

        <button>Add Product</button>
    </form>

    <hr>
    """

    for i, product in enumerate(products):
        html += f"""
        <h3>{product['name']}</h3>
        <p>Price: ₹{product['price']}</p>
        <p>Quantity: {product['quantity']}</p>

        <a href="/edit/{i}/">Edit</a> |
        <a href="/delete/{i}/">Delete</a>

        <hr>
        """

    return HttpResponse(html)


def add(request):
    if request.method == "POST":
        products.append({
            "name": request.POST["name"],
            "price": request.POST["price"],
            "quantity": request.POST["quantity"]
        })

    return home(request)


def edit(request, id):
    product = products[id]

    if request.method == "POST":
        product["name"] = request.POST["name"]
        product["price"] = request.POST["price"]
        product["quantity"] = request.POST["quantity"]

        return home(request)

    return HttpResponse(f"""
    <h2>Edit Product</h2>

    <form method="post">
        Product Name:
        <input name="name" value="{product['name']}"><br><br>

        Price:
        <input name="price" value="{product['price']}"><br><br>

        Quantity:
        <input name="quantity" value="{product['quantity']}"><br><br>

        <button>Update</button>
    </form>
    """)


def delete(request, id):
    products.pop(id)
    return home(request)


urlpatterns = [
    path("", home),
    path("add/", add),
    path("edit/<int:id>/", edit),
    path("delete/<int:id>/", delete),
]


from django.core.management import execute_from_command_line

execute_from_command_line([
    "program.py",
    "runserver",
    "0.0.0.0:8007"
])
