# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class BrandVettingTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.brand_registrations("BNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .brand_vettings.create(vetting_provider="campaign-verify")

        values = {'VettingProvider': "campaign-verify", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://messaging.twilio.com/v1/a2p/BrandRegistrations/BNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Vettings',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "AC78e8e67fc0246521490fb9907fd0c165",
                "brand_sid": "BN0044409f7e067e279523808d267e2d85",
                "brand_vetting_sid": "VT12445353",
                "vetting_provider": "campaign-verify",
                "vetting_id": "cv|1.0|tcr|10dlc|9975c339-d46f-49b7-a399-EXAMPLETOKEN|GQ3EXAMPLETOKENAXXBUNBT2AgL-LdQuPveFhEyY",
                "vetting_class": "POLITICAL",
                "vetting_status": "IN_PROGRESS",
                "date_created": "2021-01-27T14:18:35Z",
                "date_updated": "2021-01-27T14:18:35Z",
                "url": "https://messaging.twilio.com/v1/a2p/BrandRegistrations/BN0044409f7e067e279523808d267e2d85/Vettings/VT12445353"
            }
            '''
        ))

        actual = self.client.messaging.v1.brand_registrations("BNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .brand_vettings.create(vetting_provider="campaign-verify")

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.brand_registrations("BNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .brand_vettings.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://messaging.twilio.com/v1/a2p/BrandRegistrations/BNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Vettings',
        ))

    def test_read_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://messaging.twilio.com/v1/a2p/BrandRegistrations/BN0044409f7e067e279523808d267e2d85/Vettings?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "next_page_url": null,
                    "key": "data",
                    "url": "https://messaging.twilio.com/v1/a2p/BrandRegistrations/BN0044409f7e067e279523808d267e2d85/Vettings?PageSize=50&Page=0"
                },
                "data": [
                    {
                        "account_sid": "AC78e8e67fc0246521490fb9907fd0c165",
                        "brand_sid": "BN0044409f7e067e279523808d267e2d85",
                        "brand_vetting_sid": "VT12445353",
                        "vetting_provider": "campaign-verify",
                        "vetting_id": "cv|1.0|tcr|10dlc|9975c339-d46f-49b7-a399-EXAMPLETOKEN|GQ3EXAMPLETOKENAXXBUNBT2AgL-LdQuPveFhEyY",
                        "vetting_class": "POLITICAL",
                        "vetting_status": "IN_PROGRESS",
                        "date_created": "2021-01-27T14:18:35Z",
                        "date_updated": "2021-01-27T14:18:35Z",
                        "url": "https://messaging.twilio.com/v1/a2p/BrandRegistrations/BN0044409f7e067e279523808d267e2d85/Vettings/VT12445353"
                    }
                ]
            }
            '''
        ))

        actual = self.client.messaging.v1.brand_registrations("BNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .brand_vettings.list()

        self.assertIsNotNone(actual)
