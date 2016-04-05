from django.shortcuts import render
from .models import KeySignature


def note_list(request):
    keySignatures = KeySignature.objects.prefetch_related('notes').all().order_by('rootNote__name')
    return render(request, 'MainApp/note_list.html', {'keySignatures': keySignatures})
