import csv

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from .models import Bank, Branch
from .serializers import BranchSerializer

class AboutView(TemplateView):
    template_name = 'home.html'


class DetailView(View):
    def get(self, request, ifsc):
        branch = Branch.objects.filter(ifsc__iexact=ifsc).first()
        serializer = BranchSerializer(branch)
        return JsonResponse(serializer.data, safe=False)


class ListView(View):
    def get(self, request, city, bank):
        branch_qset = Branch.objects.filter(
            city__iexact=city, bank__name__icontains=bank)
        serializer = BranchSerializer(branch_qset, many=True)
        return JsonResponse(serializer.data, safe=False)
