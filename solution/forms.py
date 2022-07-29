from django.forms import ModelForm
from .models import scheduled_class
class ClassForm(ModelForm):
    class Meta:
        model=scheduled_class
        fields=('student_name','student_email','weekday','start_time','end_time')
        labels={
            'student_name':'Name',
            'student_email':'Email',
            'weekday':'Day',
            'start_time':'Start Time',
            'end_time':'End Time',
        } 
    def __init__(self,*args, **kwargs):
        super(ClassForm,self).__init__(*args, **kwargs)

        self.fields['student_name'].widget.attrs['class'] = 'form-control'
        self.fields['student_email'].widget.attrs['class'] = 'form-control'
        self.fields['weekday'].widget.attrs['class'] = 'form-control'    
        self.fields['start_time'].widget.attrs['class'] = 'form-control'    
        self.fields['end_time'].widget.attrs['class'] = 'form-control'    