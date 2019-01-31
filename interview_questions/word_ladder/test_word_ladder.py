from unittest import TestCase
from word_ladder import word_ladder


class TestWord_ladder(TestCase):

    def setUp(self):
        self.words = ['hot', 'dot', 'dog', 'lot', 'log']

    def test_word_ladder_w_out_path(self):
        start = 'hit'
        end = 'bag'
        res = word_ladder(start, end, self.words)
        self.assertIsNone(res)

    def test_word_ladder_w_path(self):
        start = 'hit'
        end = 'cog'
        res = word_ladder(start, end, self.words)
        self.assertIsNotNone(res)
