from django.shortcuts import render
from .forms import FormAddress
from . import search_address


def address(request):
    if request.method == 'POST':
        form = FormAddress(request.POST)
        if form.is_valid():
            field_location = form.cleaned_data['address']
            a = search_address.searchAddress(field_form=field_location)
            return render(request, 'result_location.html', {'form': a.address})
    else:
        form = FormAddress()

    return render(request, 'search_address.html', {'form': form})


