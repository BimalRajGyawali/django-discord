from django.shortcuts import render, redirect
from .models import Student
from .forms import UserRegisterForm
from django.views import View


def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})


def about(request):
    return render(request, 'home.html', {'name': 'about'})



def contact(request):
    if request.method == 'GET':
        print('Get req')
        return render(request, 'contact.html')

    elif request.method == 'POST':
        print('Post req')
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        email = request.POST.get('email')

        s = Student(name=name, roll=roll, email=email)
        s.save()

        return redirect('home')


#
# def register(request):
#     if request.method == 'GET':
#         form = UserRegisterForm()
#
#
#     else:
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             roll = form.cleaned_data.get('roll')
#             print(roll)
#             form.save()
#             return redirect('home')
#
#     return render(request, 'register.html', {'form': form})


class RegisterView(View):

    template = 'register.html'
    model = Student

    def get(self, request):
        form = UserRegisterForm()
        return render(request, self.template, {'form': form})


    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            roll = form.cleaned_data.get('roll')
            print('roll', roll)
            students = self.model.objects.all()
            for student in students:
                if roll == student.roll:
                    return render(request, self.template, {'form': form, 'msg': f'Roll {roll} exists'})
            else:
                form.save()
                return redirect('home')

        return render(request, self.template, {'form': form})


