from django.core.management.base import BaseCommand, CommandError
from sensor.models import (Product, SensorData)


import numpy as np

# isnert_sample_data


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        sample_prod_name = 'prod1'
        sample_data_size = 1000

        # prod = Product.objects.filter(name=sample_prod_name).all()
        # if prod:
        #     self.stdout.write(self.style.WARNING("해당하는 아이템이 이미 있습니다."))
        #     return

        # 1. 프로덕트 모델 만듬.
        prod = Product.objects.get_or_create(
            name=sample_prod_name,
        )
        # prod.save()

        for i in range(sample_data_size):
            np.random.randn(10) + 20
            sample_temperature_min = np.random.randn(10) + 20

            data = SensorData(
                product_id=prod.id,
                temp_min=sample_temperature_min)
            data.save()

        # 2. 프로덕트 아이디를 가지고 임의의 센서데이터를 만듬.(ORM Insert with For Statemnet)

        # for poll_id in options['poll_ids']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        #     self.stdout.write(self.style.SUCCESS(
        #         'Successfully closed poll "%s"' % poll_id))
