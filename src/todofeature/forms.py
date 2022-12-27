from django import forms
from todofeature.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        # exclude = ("image",)   to exclude unnecessary fields
        # fields = ("name", "description", ) to include only necessary fields
