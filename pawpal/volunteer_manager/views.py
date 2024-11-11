from django.shortcuts import render

# Example view function
def shift_list(request):
    return render(request, 'volunteer_manager/shift_list.html')
