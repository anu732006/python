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

employees = []


def home(request):
    html = """
    <h1>Employee Management</h1>

    <form method="post" action="/add/">
        Name: <input name="name"><br><br>
        Salary: <input name="salary"><br><br>
        Department: <input name="department"><br><br>
        <button>Add Employee</button>
    </form>

    <h2>Employee List</h2>
    """

    for i, e in enumerate(employees):
        html += f"""
        <p>
        {e['name']} - {e['salary']} - {e['department']}
        <a href="/delete/{i}/">Delete</a>
        </p>
        """

    return HttpResponse(html)


def add(request):
    if request.method == "POST":
        employees.append({
            "name": request.POST.get("name"),
            "salary": request.POST.get("salary"),
            "department": request.POST.get("department")
        })

    return home(request)


def delete(request, id):
    employees.pop(id)
    return home(request)


urlpatterns = [
    path("", home),
    path("add/", add),
    path("delete/<int:id>/", delete),
]


from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line([
        "program1.py", "runserver", "8004"
    ])