from django.core.management.base import BaseCommand
import csv
from datetime import datetime
from actors.models import Actor

class Command(BaseCommand):
    def add_arguments(self, parser):

        parser.add_argument(
            'file_name', 
            type=str,
            help='Nome do arquivo CSV com atores',
        )

    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                actor_name = row['name']
                actor_birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date()
                actor_nationality = row['nationality']

                self.stdout.write(self.style.NOTICE(actor_name))

                Actor.objects.create(
                    name=actor_name,
                    birthday=actor_birthday,
                    nationality=actor_nationality,
                )
        
        self.stdout.write(self.style.SUCCESS("Atores importado com sucesso!"))
        
