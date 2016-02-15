from django.shortcuts import render

def note_list(request):
    return render(request, 'MainApp/note_list.html', {})
