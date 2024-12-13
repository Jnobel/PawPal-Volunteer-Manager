from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Volunteer, Shift
from .forms import UserForm, VolunteerForm
from .forms import SignUpForm, VolunteerForm

def home(request):
    return render(request, 'home.html')  # Render the home page

def shift_list(request):
    shifts = Shift.objects.all()  # Fetch all shift objects from the database
    return render(request, 'volunteer_manager/shift_list.html', {'shifts': shifts})

def volunteer_sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page or another page after sign-up
    else:
        form = SignUpForm()

    return render(request, 'volunteer_manager/volunteer_sign_up.html', {'form': form})


@login_required
def sign_up(request, shift_id):
    shift = get_object_or_404(Shift, id=shift_id)

    # Check if the volunteer exists
    try:
        volunteer = request.user.volunteer
    except Volunteer.DoesNotExist:
        messages.error(request, "You need a volunteer profile to sign up for shifts.")
        return redirect('profile')

    # Check if the volunteer is already signed up
    if volunteer in shift.volunteers.all():
        messages.warning(request, "You have already signed up for this shift!")
    elif shift.volunteers.count() >= shift.max_volunteers:
        messages.error(request, "This shift is already full.")
    else:
        # Add the volunteer to the shift
        shift.volunteers.add(volunteer)
        shift.save()
        messages.success(request, "You have successfully signed up for the shift!")

    return HttpResponseRedirect(reverse('shift_list'))

@login_required
def drop_shift(request, shift_id):
    shift = get_object_or_404(Shift, id=shift_id)
    
    # Ensure the user is signed up for this shift
    if request.user.volunteer in shift.volunteers.all():
        shift.volunteers.remove(request.user.volunteer)
        messages.success(request, f"You have successfully dropped the shift: {shift.event_name}")
    else:
        messages.error(request, "You are not signed up for this shift.")
    
    return HttpResponseRedirect(reverse('profile'))

@login_required
def profile(request):
    try:
        # Fetch the volunteer profile for the logged-in user
        volunteer = Volunteer.objects.get(user=request.user)
        # Retrieve shifts the volunteer has signed up for
        signed_up_shifts = volunteer.shift_set.all()
    except Volunteer.DoesNotExist:
        volunteer = None
        signed_up_shifts = []

    context = {
        'user': request.user,
        'volunteer': volunteer,
        'signed_up_shifts': signed_up_shifts,
    }
    return render(request, 'volunteer_manager/profile.html', context)

@login_required
def edit_profile(request):
    try:
        volunteer = Volunteer.objects.get(user=request.user)
    except Volunteer.DoesNotExist:
        volunteer = Volunteer(user=request.user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        volunteer_form = VolunteerForm(request.POST, instance=volunteer)
        if user_form.is_valid() and volunteer_form.is_valid():
            user_form.save()
            volunteer_form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        user_form = UserForm(instance=request.user)
        volunteer_form = VolunteerForm(instance=volunteer)

    return render(request, 'volunteer_manager/edit_profile.html', {
        'user_form': user_form,
        'volunteer_form': volunteer_form,
    
    })
