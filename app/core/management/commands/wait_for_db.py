# wait_for_db
# Django가 DB가 준비될 때까지 연결을 재시도하게 해주기 위해 필요.
# 왜 이렇게 하나요? 하나의 도커 이미지에 각 컨테이너(app, db)가 존재하기 때문.

import time

from django.core.management.base import BaseCommand
from django.db import connections  # db랑 연결을 시도

from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('waiting for DB Connection ...')

        is_db_connected = None

        while not is_db_connected:
            try:
                is_db_connected = connections['default']
            except (OperationalError, Psycopg2OperationalError):
                self.stdout.write("Retry DB Connection ...")
                time.sleep(1)

        success_msg = self.style.SUCCESS('success to PostgreSQL connection')
        self.stdout.write(success_msg)
