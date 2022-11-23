import unittest
from get_subnet_and_broadcast import ip_converter

class Test_TestIPConverter(unittest.TestCase):
    def test_ip_converter(self):
        ip = "192.168.1.1/25"
        self.assertEqual(ip_converter(ip), ["192.168.1.0/25", "192.168.1.127/25"])

        ip = "192.168.1.192/28"
        self.assertEqual(ip_converter(ip), ["192.168.1.192/28", "192.168.1.207/28"])

        ip = "244.7.86.255/30"
        self.assertEqual(ip_converter(ip), ["244.7.86.252/30","244.7.86.255/30"] )
if __name__ == "__main__":
    unittest.main()