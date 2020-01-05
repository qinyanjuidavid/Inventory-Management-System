from django import forms
from myapp.models import Computer


class ComputerForm(forms.ModelForm):
    class Meta:
        model=Computer
        fields=['computer_name','IP_address','Operating_system','Mac_address','Users_name','location','purchase_date']
        def clean_computer_name(self):
            computer_name=self.cleaned_data.get('computer_name')
            if (computer_name==""):
                raise forms.ValidationError("This field can not be left blank.")
            return computer_name
        def clean_IP_address(self):
            IP_address=self.cleaned_data.get('IP_address')
            if (IP_address==""):
                raise forms.ValidationError("This field can not be left blank.")
            return IP_address
class ComputerSearch(forms.ModelForm):
    class Meta:
        model=Computer
        fields=['computer_name','Users_name']
