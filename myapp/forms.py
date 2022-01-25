from django import forms
from .models import QA
from django.forms import ModelForm

class QAData(forms.ModelForm):
	class Meta:
		model = QA
		fields = ('__all__')