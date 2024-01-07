from django.shortcuts import render, redirect
from .forms import SMSForm
from .tasks import send_sms


def main(request):
    if request.method == 'POST':
        form = SMSForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            send_sms.delay(phone_number, message)

            return redirect('success-page')
    else:
        form = SMSForm()

    return render(request, 'main.html', {'form': form})


def success(request):
    return render(request, 'success-page.html')
