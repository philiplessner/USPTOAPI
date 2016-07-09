import unittest
from unittest.mock import Mock, patch
import backend


class BackendTests(unittest.TestCase):
#    @classmethod
#    def setUpClass(cls):
#        cls.mock_get_patcher = patch('backend.requests.get')
#        cls.mock_get = cls.mock_get_patcher.start()

#    @classmethod
#    def tearDownClass(cls):
#        cls.mock_get_patcher.stop()
        
    def test_makequery(self):
        actual_payload = 'q={"_and": [{"_contains": {"assignee_organization": "KEMET"}}, {"_gte": {"patent_date": "2015-01-01"}}]}&f=["patent_date", "patent_number", "patent_title"]&o={"per_page": 50}'
        query = {'_and': [{'_contains': {'assignee_organization': 'KEMET'}}, {'_gte': {'patent_date': '2015-01-01'}}]} 
        fields = ['patent_date', 'patent_number', 'patent_title']
        options = {'per_page':50}
        predicted_payload = backend.make_query(query, fields, options)
        self.assertEqual(actual_payload, predicted_payload)
        
    def test_get_output(self):
        fields = ['patent_date', 'patent_number', 'patent_title']
        response = {'count': 17, 'total_patent_count': 17, 'patents': [{'patent_date': '2015-02-03', 'patent_title': 'Integrated EMI filter and surge protection component', 'patent_number': '8947852'}, {'patent_date': '2015-03-17', 'patent_title': 'Anode geometry with improved volumetric efficiency and improved ESR', 'patent_number': '8982536'}, {'patent_date': '2015-03-24', 'patent_title': 'High aspect ratio stacked MLCC design', 'patent_number': '8988857'}, {'patent_date': '2015-05-05', 'patent_title': 'Very large ceramic capacitor with mechanical shock resistance', 'patent_number': '9025311'}, {'patent_date': '2015-05-12', 'patent_title': 'Polymerization method for preparing conductive polymer', 'patent_number': '9030806'}, {'patent_date': '2015-05-12', 'patent_title': 'Materials and methods for improving corner and edge coverage of solid electrolytic capacitors', 'patent_number': '9030807'}, {'patent_date': '2015-06-09', 'patent_title': 'Solid electrolytic capacitor and method of manufacture', 'patent_number': '9053866'}, {'patent_date': '2015-07-21', 'patent_title': 'Asymmetric high voltage capacitor', 'patent_number': '9087648'}, {'patent_date': '2015-09-22', 'patent_title': 'Discharge capacitor', 'patent_number': '9142353'}, {'patent_date': '2015-09-29', 'patent_title': 'Hermetically sealed polymer capacitors with high stability at elevated temperatures', 'patent_number': '9147530'}, {'patent_date': '2015-10-27', 'patent_title': 'Stacked leaded array', 'patent_number': '9171672'}, {'patent_date': '2015-11-17', 'patent_title': 'Solid electrolytic capacitors with improved ESR stability', 'patent_number': '9190214'}, {'patent_date': '2016-01-12', 'patent_title': 'Materials and method for improving corner and edge coverage of solid electrolytic capacitors', 'patent_number': '9236191'}, {'patent_date': '2016-03-15', 'patent_title': 'Surface mountable multi-layer ceramic filter', 'patent_number': '9287844'}, {'patent_date': '2016-03-22', 'patent_title': 'Solid electrolytic capacitor', 'patent_number': '9293263'}, {'patent_date': '2016-04-12', 'patent_title': 'Solid electrolytic capacitor with interlayer crosslinking', 'patent_number': '9312074'}, {'patent_date': '2016-05-17', 'patent_title': 'Solid electrolytic capacitor and improved method for manufacturing a solid electrolytic capacitor', 'patent_number': '9343239'}]}
        predicted_output = backend.get_output(fields, response)
        actual_output = [('2015-02-03', '8947852', 'Integrated EMI filter and surge protection component'), ('2015-03-17', '8982536', 'Anode geometry with improved volumetric efficiency and improved ESR'), ('2015-03-24', '8988857', 'High aspect ratio stacked MLCC design'), ('2015-05-05', '9025311', 'Very large ceramic capacitor with mechanical shock resistance'), ('2015-05-12', '9030806', 'Polymerization method for preparing conductive polymer'), ('2015-05-12', '9030807', 'Materials and methods for improving corner and edge coverage of solid electrolytic capacitors'), ('2015-06-09', '9053866', 'Solid electrolytic capacitor and method of manufacture'), ('2015-07-21', '9087648', 'Asymmetric high voltage capacitor'), ('2015-09-22', '9142353', 'Discharge capacitor'), ('2015-09-29', '9147530', 'Hermetically sealed polymer capacitors with high stability at elevated temperatures'), ('2015-10-27', '9171672', 'Stacked leaded array'), ('2015-11-17', '9190214', 'Solid electrolytic capacitors with improved ESR stability'), ('2016-01-12', '9236191', 'Materials and method for improving corner and edge coverage of solid electrolytic capacitors'), ('2016-03-15', '9287844', 'Surface mountable multi-layer ceramic filter'), ('2016-03-22', '9293263', 'Solid electrolytic capacitor'), ('2016-04-12', '9312074', 'Solid electrolytic capacitor with interlayer crosslinking'), ('2016-05-17', '9343239', 'Solid electrolytic capacitor and improved method for manufacturing a solid electrolytic capacitor')]
        self.assertListEqual(actual_output, predicted_output)
   
    def test_get_info(self):
        API_ENDPOINT = 'http://www.patentsview.org/api/patents/query'
        payload = 'q={"_and":[{"_contains": {"assignee_organization": "KEMET"}}, {"_gte": {"patent_date": "2015-01-01"}}]}&f=["patent_date", "patent_number", "patent_title"]&o={"per_page": 50}'
        patent_response = {'count': 17, 'total_patent_count': 17, 'patents': [{'patent_date': '2015-02-03', 'patent_title': 'Integrated EMI filter and surge protection component', 'patent_number': '8947852'}, {'patent_date': '2015-03-17', 'patent_title': 'Anode geometry with improved volumetric efficiency and improved ESR', 'patent_number': '8982536'}, {'patent_date': '2015-03-24', 'patent_title': 'High aspect ratio stacked MLCC design', 'patent_number': '8988857'}, {'patent_date': '2015-05-05', 'patent_title': 'Very large ceramic capacitor with mechanical shock resistance', 'patent_number': '9025311'}, {'patent_date': '2015-05-12', 'patent_title': 'Polymerization method for preparing conductive polymer', 'patent_number': '9030806'}, {'patent_date': '2015-05-12', 'patent_title': 'Materials and methods for improving corner and edge coverage of solid electrolytic capacitors', 'patent_number': '9030807'}, {'patent_date': '2015-06-09', 'patent_title': 'Solid electrolytic capacitor and method of manufacture', 'patent_number': '9053866'}, {'patent_date': '2015-07-21', 'patent_title': 'Asymmetric high voltage capacitor', 'patent_number': '9087648'}, {'patent_date': '2015-09-22', 'patent_title': 'Discharge capacitor', 'patent_number': '9142353'}, {'patent_date': '2015-09-29', 'patent_title': 'Hermetically sealed polymer capacitors with high stability at elevated temperatures', 'patent_number': '9147530'}, {'patent_date': '2015-10-27', 'patent_title': 'Stacked leaded array', 'patent_number': '9171672'}, {'patent_date': '2015-11-17', 'patent_title': 'Solid electrolytic capacitors with improved ESR stability', 'patent_number': '9190214'}, {'patent_date': '2016-01-12', 'patent_title': 'Materials and method for improving corner and edge coverage of solid electrolytic capacitors', 'patent_number': '9236191'}, {'patent_date': '2016-03-15', 'patent_title': 'Surface mountable multi-layer ceramic filter', 'patent_number': '9287844'}, {'patent_date': '2016-03-22', 'patent_title': 'Solid electrolytic capacitor', 'patent_number': '9293263'}, {'patent_date': '2016-04-12', 'patent_title': 'Solid electrolytic capacitor with interlayer crosslinking', 'patent_number': '9312074'}, {'patent_date': '2016-05-17', 'patent_title': 'Solid electrolytic capacitor and improved method for manufacturing a solid electrolytic capacitor', 'patent_number': '9343239'}]}
       
        with patch('backend.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value.total_patent_count = 17
            mock_get.return_value.json.return_value = patent_response
            info = backend.get_info(payload, base=API_ENDPOINT)
        self.assertIsNotNone(info)
        self.assertDictEqual(info, patent_response)
        
       
if __name__ == '__main__':
    unittest.main()    
