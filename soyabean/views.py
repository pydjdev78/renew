from django.shortcuts import render
from .models import Collect, Process

def func_one(request, id1):
	c_list = Collect.objects.all()
	context = {"it_list": c_list, "id1": id1}
	print(dir(c_list))
	print(type(c_list))
	print(c_list.all())
	return render(request, "soyabean/bean1.html", context)

def func_two(request, id1, id2):
	p_list = Process.objects.all()
	context = {"it_list": p_list, "id1": id1, "id2": id2}
	return render(request, "soyabean/bean2.html", context)

def func_three(request, id1, id2, id3):
	return render(request, "soyabean/bean3.html")

def func_four(request, id1, id2, id3, id4):
	return render(request, "soyabean/bean4.html")