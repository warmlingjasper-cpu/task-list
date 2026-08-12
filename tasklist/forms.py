from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 5,
                "cols": 50,
                "class": "form-control",
                "placeholder": "Describe your task...",
            }
        )
    )

    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "status",
            "start_date",
            "end_date",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control title-input",
                    "placeholder": "Task title",
                }
            ),
            "status": forms.Select(
                attrs={
                    "class": "form-select status-input",
                }
            ),
            "start_date": forms.DateInput(
                attrs={
                    "class": "form-control date-input",
                    "type": "date",
                }
            ),
            "end_date": forms.DateInput(
                attrs={
                    "class": "form-control date-input",
                    "type": "date",
                }
            ),
        }


    def clean(self):
        cleaned_data = super().clean()

        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date and end_date < start_date:
            raise forms.ValidationError(
                "End date cannot be earlier than start date."
            )

        return cleaned_data