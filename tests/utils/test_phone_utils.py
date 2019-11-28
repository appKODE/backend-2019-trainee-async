from utils import phone


class TestPhoneUtils:
    def test_phone_utils(self):
        phone_number = '+79113334455'
        expected = '89113334455'

        cases = [
            dict(
                phone_number='+79113334455',
                expected='89113334455',
            ),
            dict(
                phone_number='+79113',
                expected='+79113',
            ),
            dict(
                phone_number='+489113334455',
                expected='+489113334455',
            ),
        ]

        for case in cases:
            assert phone.prepare_phone_number(case['phone_number']) == case['expected']

