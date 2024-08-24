from django import forms

from my_app.models import Items, Category, Review


# class ItemCreationForm(forms.Form):
#     name = forms.CharField(max_length=50)
#     description = forms.CharField(widget=forms.Textarea(
#         attrs={'class': 'description', 'rows': 3}
#     ))
#     price = forms.IntegerField()
#     count = forms.IntegerField(required=False)
#     # category_id = forms.ChoiceField(
#     #     choices=((1, 'Первый'), (2, 'Второй'))
#     #                                 )
#     category_id = forms.ModelChoiceField(
#         queryset=Category.objects.all(),
#         required=True
#     )
class ItemCreationForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'description', 'price', 'count', 'category', 'picture']

class CatCreationForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'content', 'rating', 'image', 'show', 'product']
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, i) for i in range(1, 6)])
        }