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

customers = []


def home(request):
    html = """
    <h1>Customer Management</h1>

    <form method="post" action="/add/">
        Name: <input name="name"><br><br>
        Phone: <input name="phone"><br><br>
        City: <input name="city"><br><br>
        <button>Add Customer</button>
    </form>

    <h2>Customer List</h2>
    """

    for i, c in enumerate(customers):
        html += f"""
        <p>
        {c['name']} - {c['phone']} - {c['city']}
        <a href="/delete/{i}/">Delete</a>
        </p>
        """

    return HttpResponse(html)


def add(request):
    if request.method == "POST":
        customers.append({
            "name": request.POST.get("name"),
            "phone": request.POST.get("phone"),
            "city": request.POST.get("city")
        })

    return home(request)


def delete(request, id):
    customers.pop(id)
    return home(request)


urlpatterns = [
    path("", home),
    path("add/", add),
    path("delete/<int:id>/", delete),
]


from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line([
        "program4.py", "runserver", "8000"
    ])