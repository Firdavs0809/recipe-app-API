from django.test import SimpleTestCase


class JustTestCase(SimpleTestCase):
    def test_addition(self):
        self.assertEqual(2, 2)
