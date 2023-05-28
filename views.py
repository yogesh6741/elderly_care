from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import ElderlyPerson, Medication

def medication_list(request, elderly_person_id):
    elderly_person = get_object_or_404(ElderlyPerson, id=elderly_person_id)
    medications = Medication.objects.filter(elderly_person=elderly_person)
    return render(request, 'medication_list.html', {'elderly_person': elderly_person, 'medications': medications})

def send_medication_reminder(request, medication_id):
    medication = get_object_or_404(Medication, id=medication_id)
    reminder_message = f"It's time to take your medication - {medication.name}"
    return HttpResponse("Reminder sent!")
