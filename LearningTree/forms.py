from django import forms
from models import *

class NodeForm(forms.ModelForm):
 class Meta:
  model = Node
  #Put the fields in order.
  fields = ["name","content"]

