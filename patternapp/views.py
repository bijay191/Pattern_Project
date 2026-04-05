from django.shortcuts import render
from .models import FileName, RegexPattern
from .utils import generate_regex


def generate_patterns(request):
    filenames = FileName.objects.all()

    for file in filenames:
        regex = generate_regex(file.name)

        # Avoid duplicate entries
        RegexPattern.objects.get_or_create(
            file=file,
            pattern=regex
        )

    return render(request, 'result.html', {'patterns': RegexPattern.objects.all()})