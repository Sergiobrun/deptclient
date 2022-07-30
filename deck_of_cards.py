import json
import requests
import unittest


import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class regression(unittest.TestCase):

    def test_amount_of_cards(self):

        # Shuffle the cards and get deck_id
        shuffle_endpoint = "https://deckofcardsapi.com/api/deck/new/shuffle"
        payload_1 = {'deck_count': '1'}
        resp = requests.post(shuffle_endpoint, params=payload_1)
        shuffle_endpoint_resp = json.loads(resp.text)
        original_amount_of_cards = shuffle_endpoint_resp["remaining"]
        deck_id = (shuffle_endpoint_resp["deck_id"])

        # Draw cards
        base_draw_enpoint = "https://deckofcardsapi.com/api/deck/{}/draw/"
        draw_enpoint = base_draw_enpoint.format(deck_id)
        payload_2 = {'count': '3'}
        resp = requests.post(draw_enpoint, params=payload_2)
        draw_enpoint_resp = json.loads(resp.text)
        remaining = (draw_enpoint_resp["remaining"])

        # Test
        self.assertTrue(int(original_amount_of_cards) - 1 == int(remaining))
        #self.assertTrue(int(original_amount_of_cards) - int(payload_2["count"]) == int(remaining))
