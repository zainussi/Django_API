from import_export import resources
from .models import QA

class QAResource(resources.ModelResource):
    class Meta:
        model = QA