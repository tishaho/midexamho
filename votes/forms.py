from django.forms import ModelForm
from .models import Candidate
from .models import Position
from .models import Vote


class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        exclude = ['id']
        exclude = ['position']


class PositionForm(ModelForm):
    class Meta:
        model = Position
        exclude = ['id']
