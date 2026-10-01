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

employees = []


def home(request):
    html = """
    <h1>Employee Management</h1>

    <form method="post" action="/add/">
        Name: <input name="name"><br><br>
        Department: <input name="department"><br><br>
        Salary: <input name="salary"><br><br>
        <button>Add Employee</button>
    </form>
    <hr>
    """

    for i, employee in enumerate(employees):
        html += f"""
        <h3>{employee['name']}</h3>
        <p>Department: {employee['department']}</p>
        <p>Salary: {employee['salary']}</p>

        <a href="/edit/{i}/">Edit</a> |
        <a href="/delete/{i}/">Delete</a>
        <hr>
        """

    return HttpResponse(html)


def add(request):
    if request.method == "POST":
        employees.append({
            "name": request.POST["name"],
            "department": request.POST["department"],
            "salary": request.POST["salary"]
        })

    return home(request)


def edit(request, id):
    employee = employees[id]

    if request.method == "POST":
        employee["name"] = request.POST["name"]
        employee["department"] = request.POST["department"]
        employee["salary"] = request.POST["salary"]

        return home(request)

    return HttpResponse(f"""
    <h2>Edit Employee</h2>

    <form method="post">
        Name:
        <input name="name" value="{employee['name']}"><br><br>

        Department:
        <input name="department" value="{employee['department']}"><br><br>

        Salary:
        <input name="salary" value="{employee['salary']}"><br><br>

        <button>Update</button>
    </form>
    """)


def delete(request, id):
    employees.pop(id)
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
    "0.0.0.0:8004"
])
