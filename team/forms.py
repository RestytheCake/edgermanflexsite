from django import forms

from .models import FileUpload, NickUser, forum, comment, notification, profile
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['file']


class addforum(forms.ModelForm):
    class Meta:
        model = forum
        fields = ['title', 'message', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'id': 'createTopic'}),
            'message': forms.Textarea(attrs={'id': 'createDesc'}),
            'tags': forms.TextInput(attrs={'id': 'keywords'})
        }


class commentform(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['comments']
        widgets = {
            'comments': forms.Textarea(attrs={'id': 'commentInput'})
        }


class profileform(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['special']


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = NickUser
        fields = ('username', 'password', 'last_login', 'active', 'discord_member', 'supporter', 'special', 'confirm', 'staff', 'admin',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = NickUser
        fields = ('username', 'password', 'last_login', 'active', 'discord_member', 'supporter', 'special', 'confirm', 'staff', 'admin',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class notify(forms.ModelForm):
    class Meta:
        model = notification
        fields = ['User',
                  'Description',
                  'Warning',
                  'Sender']
