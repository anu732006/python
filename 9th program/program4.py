import django
from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY="123",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
)

django.setup()

from django.http import HttpResponse
from django.urls import path

books = []


def home(request):
    html = """
    <h1>Book Management</h1>

    <form method="post" action="/add/">
        Book Name: <input name="name"><br><br>
        Author: <input name="author"><br><br>
        Price: <input name="price"><br><br>
        <button>Add Book</button>
    </form>

    <h2>Book List</h2>
    """

    for i, b in enumerate(books):
        html += f"""
        <p>
        {b['name']} - {b['author']} - ₹{b['price']}
        <a href="/delete/{i}/">Delete</a>
        </p>
        """

    return HttpResponse(html)


def add(request):
    if request.method == "POST":
        books.append({
            "name": request.POST.get("name"),
            "author": request.POST.get("author"),
            "price": request.POST.get("price")
        })

    return home(request)


def delete(request, id):
    books.pop(id)
    return home(request)


urlpatterns = [
    path("", home),
    path("add/", add),
    path("delete/<int:id>/", delete),
]


from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line([
        "program2.py", "runserver", "8000"
    ])