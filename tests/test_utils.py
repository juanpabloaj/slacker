import unittest

from slacker.utils import id_from_list_dict


class TestUtils(unittest.TestCase):

    def test_id_from_list_dict(self):
        list_dict = [{'name': 'channel_name', 'id': '123'}, {}]

        self.assertEqual(
            '123', id_from_list_dict(list_dict, 'channel_name')
        )
