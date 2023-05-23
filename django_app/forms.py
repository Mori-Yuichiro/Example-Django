from django import forms
from django.core import validators

from .models import Memo


class MemoForm(forms.ModelForm):
    memo = forms.CharField(widget=forms.Textarea)
    # 別のバリデーション記載法
    # memo = forms.CharField(widget=forms.Textarea, validators=[
    #                        validators.MaxLengthValidator(200, '200文字以内にしてください')])
    # memo = forms.CharField(required=True)

    class Meta:
        model = Memo
        fields = ('memo',)

    def clean_memo(self):
        print('---------- clean_name ---------------')
        memo = self.cleaned_data['memo']
        print(memo)
        if len(memo) > 200:
            print('エラー')
            raise forms.ValidationError('メモは200文字以内にしてください')

        return memo
