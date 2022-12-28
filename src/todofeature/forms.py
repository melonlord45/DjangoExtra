from django import forms
from todofeature.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["name"].widget.attrs["class"] = "form-control"
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            # self.fileds()

        # exclude = ("image",)   to exclude unnecessary fields
        # fields = ("name", "description", ) to include only necessary fields

    def clean_name(self):  # to validate specific filed
        name = self.cleaned_data.get("name")
        if name.isdigit():
            raise forms.ValidationError("Name cannot be in numbers")
        return name
        