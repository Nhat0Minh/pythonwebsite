from django.forms import ModelForm, ValidationError

class UserProfileCreationForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 3:
            raise ValidationError('Username must be at least 3 characters long.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@example.com'):
            raise ValidationError('Email must end with @example.com')
        return email

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise ValidationError('Passwords must match.')
        return password1

def login_view(request):
    form = AuthenticationForm(request.POST or None)

    if form.is_valid():
        user = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=user, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'form': form})

    return render(request, 'login.html', {'form': form})

def registration_view(request):
    form = UserProfileCreationForm(request.POST or None)

    if form.is_valid():
        try:
            form.save()
        except ValidationError as e:
            return render(request, 'register.html', {'form': form, 'errors': e.errors})
        return redirect('login')

    return render(request, 'register.html', {'form': form})





    