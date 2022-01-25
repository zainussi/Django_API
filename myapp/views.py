import pandas as pd
from django.contrib import messages
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import permission_required
from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework.decorators import action
from django.shortcuts import render
from rest_framework.response import Response
from .serializers import QASerializer
from .models import QA,ExcelFile
from django.contrib import messages
from tablib import Dataset
from django.http import JsonResponse
from django.conf import settings
from .resources import QAResource

class QAViewSet(viewsets.ModelViewSet):
    queryset = QA.objects.all().order_by('question')
    serializer_class = QASerializer

def import_data_to_db(request):
    if request.method =='POST':
        qa_resource = QAResource()
        file = request.FILES['files']
        obj = ExcelFile.objects.create(
            file = file
        )
        path = str(obj.file)
        print(f'{settings.BASE_DIR}/{path}')
        df = pd.read_excel(path)
        for i in df.values:
            print(i)
    return render(request, 'input.html')
