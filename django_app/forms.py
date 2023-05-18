from django import forms


class MemoForm(forms.Form):
    # memo = forms.CharField(widget=forms.Textarea)
    memo = forms.CharField(required=True)

    # def clean_memo(self):
    #     memo = self.cleaned_data['memo']
    #     print('確認')
    #     if len(memo) > 20:
    #         raise forms.ValidationError('メモは200文字以内にしてください')
