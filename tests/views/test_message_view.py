AUTH_HEADER = {'Authorization': "Bearer 123123123"}


class TestMessage:
    async def test_message_success(self, client, mock_message_data):
        expected_status = 200
        resp = await client.post(
            '/api/pitter/v1/message',
            json=mock_message_data,
            headers=AUTH_HEADER,
        )

        assert resp.status == expected_status

    async def test_message_fail_auth(self, client, mock_message_data):
        expected_status = 401
        resp = await client.post(
            '/api/pitter/v1/message',
            json=mock_message_data,
        )

        assert resp.status == expected_status

    # TODO: проверить ошибки валидации входных параметров
