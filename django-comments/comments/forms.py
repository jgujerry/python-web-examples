
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Column, Layout, Row, Submit
from tinymce.widgets import TinyMCE

from comments import Comment


CUSTOM_MCE_ATTRS = {
    'theme': 'silver',
    'height': 300,
    'width': '100%',
    'menubar': False,
    'plugins': 'advlist,autolink,lists,link,image,charmap,print,preview,anchor,'
      'searchreplace,visualblocks,code,fullscreen,insertdatetime,media,table,paste'
      'code,help,wordcount',
    'toolbar': 'bold italic underline strikethrough forecolor backcolor |'
      'bullist numlist outdent indent | alignleft alignright alignjustify |'
      'link | removeformat help',
}


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='New Comment', widget=TinyMCE(mce_attrs=CUSTOM_MCE_ATTRS))
    
    class Meta:
        model = Comment
        fields = ('content',)
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
          Row(Column('content', css_class='form-group col-md-12 mb-0'),),
          ButtonHolder(Submit(type='submit', name='buttonValue', value='Add Comment', css_class='btn btn-warning'))
        )
