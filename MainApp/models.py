from django.db import models


# from django_enumfield import enum


# class Notes(enum):
# 	Ab = 1
# 	A = 2
# 	ASharp = 3
# 	Bb = 4
# 	B = 5
# 	C = 6
# 	CSharp = 7
# 	Db = 8
# 	D = 9
# 	DSharp = 10
# 	Eb = 11
# 	E = 12
# 	F = 13
# 	FSharp = 14
# 	GFlat = 15
# 	G = 16
# 	GSharp = 17

# class Notes(models.Model):
# 	A = 1
# 	B = 2
# 	C = 3
# 	D = 4
# 	E = 5
# 	F = 6
# 	G = 7

# Note to KeySignature is a many to many, needs intermediate table for ordering

# use one choices field for normal/sharp/flat
class Note(models.Model):
    NAME_CHOICES = (
        ('A', 'A'),
        ('Ab', 'Ab'),
        ("A#", "A#"),
        ('B', 'B'),
        ('Bb', 'Bb'),
        ('C', 'C'),
        ("C#", "C#"),
        ('D', 'D'),
        ('Db', 'Db'),
        ("D#", "D#"),
        ('E', 'E'),
        ('Eb', 'Eb'),
        ('F', 'F'),
        ("F#", "F#"),
        ('G', 'G'),
        ('Gb', 'Gb'),
        ("G#", "G#"),
    )
    name = models.CharField(max_length=2,
                            choices=NAME_CHOICES,
                            default='A')
    isSharp = models.BooleanField(default=False)
    isFlat = models.BooleanField(default=False)

    # sharpNote = models.OneToOneField(Note)
    # flatNote = models.OneToOneField(Note)
    # hasSharp = models.BooleanField
    # hasFlat = models.BooleanField

    def __str__(self):
        return self.name


class KeySignature(models.Model):
    # Look up extra fields on Many-To-Many Relations
    rootNote = models.ForeignKey(Note, related_name="root", null=True)
    notes = models.ManyToManyField(Note,
                                   through='KeySignatureNote'
                                   )

    def __str__(self):
        return self.rootNote.name


class KeySignatureNote(models.Model):
    note = models.ForeignKey(Note)
    keySignature = models.ForeignKey(KeySignature)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return 'Key: ' + self.keySignature.rootNote.name + ', Note: ' + self.note.name

