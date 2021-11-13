from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Employees, Department
from EmployeeApp.serializers import DepartmentSerializers,EmployeeSerializers

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def employeeApi(request,id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializers( employees , many= True)
        return JsonResponse(employees_serializer.data , safe = False)

    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializers(data = employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Succesfully !", safe=False)
        return JsonResponse("Failed to add." , safe=False)

    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employees = Employees.objects.get(EmployeeId = employee_data['EmployeeId'])
        employees_serializer = EmployeeSerializers(employees,data = employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("updated Successfully !", safe = False)
        return JsonResponse("Failed to Update.", safe = False)

    elif request.method == 'DELETE':
        employees = Employees.objects.get(EmployeeId = id)
        employees.delete()
        return JsonResponse("Deleted Successfully !", safe = False)





@csrf_exempt
def departmentApi(request,id=0):
    if request.method == 'GET':
        departments = Department.objects.all()
        departments_serializer = DepartmentSerializers( departments , many= True)
        return JsonResponse(departments_serializer.data , safe = False)

    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializers(data = department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Succesfully !", safe=False)
        return JsonResponse("Failed to add." , safe=False)

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Department.objects.get(DepartmentId = department_data['DepartmentId'])
        department_serializer = DepartmentSerializers(department,data = department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("updated Successfully !", safe = False)
        return JsonResponse("Failed to Update.", safe = False)

    elif request.method == 'DELETE':
        department = Department.objects.get(DepartmentId = id)
        department.delete()
        return JsonResponse("Deleted Successfully !", safe = False)       


@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe= False)