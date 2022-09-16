from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get("title")
        if title.lower().strip() == "taha":
            self.add_error("title", "taha is taken")
            raise forms.ValidationError("taha is not allowed")

        return cleaned_data
