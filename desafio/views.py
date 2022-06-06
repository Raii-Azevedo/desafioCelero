import codecs
import csv

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from .serializers import AthleteSerializer

from .models import Athlete

fs = FileSystemStorage(location='tmp/')


# Viewset
class AthleteViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the Athletes data.
    """
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer

    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        file = request.FILES['file']

        content = file.read()
        file_content = ContentFile(content)
        file_name = fs.save(
            "tmp.csv", file_content
        )
        tmp_file = fs.path(file_name)

        csv_file = open(tmp_file, errors="ignore")
        reader = csv.reader(csv_file)
        next(reader)

        athletes_list = []

        for id_, row in enumerate(reader):
            (
                name_id,
                sex,
                age,
                height,
                weight,
                team,
                noc,
                games,
                year,
                season,
                city,
                sport,
                event,
                medal,
            ) = row

            athletes_list.append(
                Athlete(
                    name= name_id,
                    sex =sex,
                    age = age,
                    height = height,
                    weight = weight,
                    team = team,
                    noc = noc,
                    games = games,
                    year = year,
                    season = season,
                    city = city,
                    sport = sport,
                    event = event,
                    medal = medal,
                    )
            )

        Athlete.objects.bulk_create(athletes_list)

        return Response("Arquivo carregado corretamente")




