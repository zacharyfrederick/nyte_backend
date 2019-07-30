import stripe

class Stripe_Manager():

    def create_charge(self, card,customer, amount):
        try:
            self.response = stripe.Charge.create(card=card, customer=customer, amount=amount, description="Charge from Nyte App", currency="usd", capture="true")
            return
        except stripe.error.CardError as e:
            self.error_code = "CardError"
        except stripe.error.RateLimitError as e:
            self.error_code = "RateLimitError"
        except stripe.error.InvalidRequestError as e:
            self.error_code = "InvalidRequestError"
            print(e)
        except stripe.error.AuthenticationError as e:
            self.error_code = "AuthenticationError"
        except stripe.error.APIConnectionError as e:
            self.error_code = "APIConnectionError"
        except stripe.error.StripeError as e:
            self.error_code = "StripeError"
        except Exception as e:
            self.error_code = "Unknown"
        self.response = None

    def get_failure_code(self):
        if self.response is not None:
            failure_code = self.response['failure_code']
            failure_code = "None" if failure_code == None else failure_code
            return failure_code
        else:
            return self.error_code
        
    def get_failure_message(self):
        if self.response is not None:
            return self.response['failure_message']

    def get_paid(self):
        if self.response is not None:
            return self.response['paid']

    def get_transaction_id(self):
        if self.response is not None:
            return self.response['id']

    def get_payment(self):
        if self.response is not None:
            return self.response['payment_method']