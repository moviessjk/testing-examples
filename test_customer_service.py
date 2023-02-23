import unittest
from unittest.mock import patch

from customer_service import customer_signup


class UnitTestCustomerService(unittest.TestCase):
    @patch("customer_service.register")
    @patch("uuid.uuid4")
    def test_customer_service_signup(self, mock_uuid, mock_register):
        mock_uuid.return_value = "1"
        customer_signup("Pedro", 42)
        mock_uuid.assert_called_once()
        mock_register.assert_called_once_with("Pedro", 42, "1")
