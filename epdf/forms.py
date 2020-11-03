from django import forms
from .models import Document, Category_Name


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category_Name

        exclude = [
            "Category_name"
        ]


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document

        fields = [
            "title",
            "description",
            "document",
            "category",
            "author",
            "image"
        ]
