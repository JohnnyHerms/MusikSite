from django.contrib import admin
from .models import Note
from .models import KeySignature
from .models import KeySignatureNote


class KeySignatureNoteInline(admin.TabularInline):
    model = KeySignatureNote


class NoteAdmin(admin.ModelAdmin):
    inlines = (KeySignatureNoteInline,)


class KeySignatureAdmin(admin.ModelAdmin):
    inlines = (KeySignatureNoteInline,)

admin.site.register(Note, NoteAdmin)
admin.site.register(KeySignature, KeySignatureAdmin)
admin.site.register(KeySignatureNote)
# admin.site.register(KeySignatureAdmin)
# admin.site.register(NoteAdmin)
