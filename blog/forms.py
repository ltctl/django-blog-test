# from django import forms
# from .models import Article, Tag, Comment, Blogger
#
# TYPE_CHOICES = ('Philosophy', 'Science', 'Art', 'Technology', 'Relationships')
#
#
# # class ArticleForm(forms.Form):
# #     title = forms.CharField(help_text="Enter the title.", max_length=20)
# #     content = forms.CharField(widget=forms.Textarea)
# #     date_time = forms.DateField
# #     about = forms.MultipleChoiceField(
# #             required=False,
# #             widget=forms.CheckboxSelectMultiple,
# #             choices=TYPE_CHOICES,)
# #
# #     title.widget.attrs.update({'class': 'special'}, size='40')
#
# class ArticleForm(forms.Form):
#     class Meta:
#         model = Article
#         fields = '__all__'
