from django import forms
from .models import QA

class QAData(forms.Form):
	class meta:
		model = QA
		fields = '__all__'