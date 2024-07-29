import unittest
import json
from app import app

# Setting up the Flask test client
class RuleEngineTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def create_rule(self, rule):
        return self.app.post('/create_rule', data=json.dumps({'rule': rule}), content_type='application/json')

    def combine_rules(self, rules):
        return self.app.post('/combine_rules', data=json.dumps({'rules': rules}), content_type='application/json')

    def evaluate_rule(self, ast, data):
        return self.app.post('/evaluate_rule', data=json.dumps({'ast': ast, 'data': data}), content_type='application/json')
