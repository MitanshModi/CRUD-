from django.shortcuts import redirect, render
from app.models import Employees


def INDEX(request):
    # Correct the query for fetching all employees
    emp = Employees.objects.all()

    context = {
        'emp': emp,
    }

    return render(request, 'index.html', context)


def ADD(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        # Create and save new employee
        emp = Employees(
            name=name,
            email=email,
            address=address,
            phone=phone
        )
        emp.save()
        return redirect('home')  # Correct syntax for redirect

    return render(request, 'index.html')  # If not POST, just render the page


def Edit(request, id):
    emp = Employees.objects.get(id=id)  # Fetch the employee by ID

    context = {
        'emp': emp,
    }

    return render(request, 'edit_employee.html', context)  # Return the edit form for this employee


def Update(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees.objects.get(id=id)  # Fetch the employee by ID

        # Update the employee object
        emp.name = name
        emp.email = email
        emp.address = address
        emp.phone = phone

        emp.save()  # Save the updated employee
        return redirect('home')  # Redirect after successful update

    return redirect('home')  # If not POST, redirect


def Delete(request, id):
    emp = Employees.objects.get(id=id)  # Fetch the employee by ID
    emp.delete()  # Delete the employee object
    return redirect('home')  # Redirect after deletion
