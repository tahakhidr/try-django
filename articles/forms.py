from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'publish']

    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs = Article.objects.filter(title__iexact=title)
        if qs.exists():
            self.add_error("title", f"\"{title}\" is already in use.")
        return data


# class ArticleForm(forms.Form):
#     title = forms.CharField()
#     content = forms.CharField()

#     def clean(self):
#         cleaned_data = self.cleaned_data
#         title = cleaned_data.get("title")
#         if title.lower().strip() == "taha":
#             self.add_error("title", "taha is taken")
#             raise forms.ValidationError("taha is not allowed")

#         return cleaned_data
