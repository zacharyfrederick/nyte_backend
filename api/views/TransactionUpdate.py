#python imports
import json

#django imports
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
import django

#DRF imports
from rest_framework.views import APIView
from rest_framework.response import Response

#Nyte imports
from ..managers import FacebookManager
from .. import models
import datetime

from twilio.base.exceptions import TwilioRestException


class UnacceptableStatusError(Exception):
    pass

class TransactionUpdate(APIView):
    acceptable_statuses = ["submitted", "in progress", "completed", "picked up", "canceled"]

    def __init__(self):
        self.canceled_reason = None

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        try:
            self.get_parameters(request)
            self.attempt_to_find_transaction()
            self.validate_status()
            self.update_status()
            self.get_canceled_reason()
            self.update_status()
            self.transaction.check_for_status_updates()
            self.transaction.save()
        except KeyError:
            return Response({"error": "you did not submit the proper attributes"})
        except json.JSONDecodeError:
            return Response({"error": "error decoding body"})
        except models.Transaction.DoesNotExist:
            return Response({"error": "no transaction with that id"})
        except UnacceptableStatusError:
            return Response({"error": "an unacceptable response was sent in"})
        except TwilioRestException:
            return Response({"error": "There was an error sending a text notification"})
        return Response({"success": "transaction updated sucessfully"})

    def get_parameters(self, request):
        self.body_formatted = json.loads(request.body)
        self.transaction_id = self.body_formatted['id']
        self.status = self.body_formatted['status']

    def attempt_to_find_transaction(self):
        self.transaction = models.Transaction.objects.get(id=self.transaction_id)

    def validate_status(self):
        if self.status not in self.acceptable_statuses:
            raise UnacceptableStatusError

    def get_canceled_reason(self):
        if self.status == "canceled":
            self.canceled_reason = self.body_formatted['canceled_reason']

    def update_status(self):
        self.transaction.status = self.status
        self.update_times_if_necessary()

    def update_times_if_necessary(self):
        if self.status == "canceled":
            if self.canceled_reason is not None:
                self.transaction.cancel_reason = self.canceled_reason
                self.transaction.canceled = now()
                return
        if self.status == "completed":
            self.transaction.ready = now()
            return 
        if self.status == "picked up":
            self.transaction.complete = now()