import logging

from django.core.management.base import BaseCommand
from django.db import connection

from mailer.models import MessageLog


class Command(BaseCommand):
    help = "Clean the message log table."

    def add_arguments(self, parser):
        parser.add_argument('-c, --cron', dest='cron', action='store_const',
                            default=0, const=1)

    def handle_noargs(self, **options):
        if options['cron'] == 0:
            logging.basicConfig(level=logging.DEBUG, format="%(message)s")
        else:
            logging.basicConfig(level=logging.ERROR, format="%(message)s")
        all_messages = MessageLog.objects.all()
        logging.debug("Deleting %d message log objects..." % len(all_messages))
        all_messages.delete()
        logging.debug("Done.")
        connection.close()
