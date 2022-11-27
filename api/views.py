from django.shortcuts import render
from .models import Student
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io 
from .serializers import StudentSerializer

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.

@method_decorator(csrf_exempt,name = 'dispatch')

class StudentAPI(View):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            std = Student.objects.get(id = id)
            serializer = StudentSerializer(std)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'application/json')
        std = Student.objects.all()
        serializer = StudentSerializer(std,many= True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type = 'application/json')

    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            r = {'msg':'Data saved'}
            json_data = JSONRenderer().render(r)
            return HttpResponse(json_data,content_type ='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type ='application/json')
    def put(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id= id) 
        #serializer = StudentSerializer(stu, data = python_data,partial = True) - for partial update
        serializer = StudentSerializer(stu, data = python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            re = {'msg':'Data updated'}
            json_data = JSONRenderer().render(re)
            return HttpResponse(json_data,content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type = 'application/json')

    def delete(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        re = {'msg':'Data deleted'}
        #json_data = JSONRenderer().render(re)
        #return HttpResponse(json_data,content_type = 'application/json')
        return JsonResponse(re, safe=False)
        
        