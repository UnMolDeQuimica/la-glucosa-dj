from django.forms import ModelForm, TextInput
from .models import GlucoseRecord

class CreateGlucoseRecordForm(ModelForm):
    class Meta:
        model = GlucoseRecord
        exclude = ["user"]
        
        widgets = {
            "date": TextInput(attrs={"type": "datetime-local"})
        }
