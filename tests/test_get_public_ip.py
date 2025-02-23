import pytest
import requests
from unittest.mock import patch
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from get_public_ip import get_public_ip

class TestGetPublicIP:
    def test_get_public_ip_success(self):
        """Test successful retrieval of public IP"""
        with patch('requests.get') as mock_get:
            # Mock a successful response with a valid IP
            mock_response = mock_get.return_value
            mock_response.status_code = 200
            mock_response.text = '8.8.8.8'
            
            ip = get_public_ip()
            assert ip == '8.8.8.8'
    
    def test_get_public_ip_network_error(self):
        """Test handling of network errors"""
        with patch('requests.get') as mock_get:
            # Simulate a network error
            mock_get.side_effect = requests.RequestException("Network error")
            
            with pytest.raises(ConnectionError):
                get_public_ip()
    
    def test_get_public_ip_bad_status_code(self):
        """Test handling of bad HTTP status codes"""
        with patch('requests.get') as mock_get:
            # Mock a failed response
            mock_response = mock_get.return_value
            mock_response.status_code = 500
            
            with pytest.raises(ConnectionError):
                get_public_ip()
    
    def test_get_public_ip_invalid_ip_format(self):
        """Test handling of invalid IP formats"""
        with patch('requests.get') as mock_get:
            # Mock response with invalid IP
            mock_response = mock_get.return_value
            mock_response.status_code = 200
            
            # Test various invalid IP formats
            invalid_ips = [
                '256.0.0.1',   # Out of range
                '1.2.3.4.5',   # Too many octets
                'not.an.ip',   # Non-numeric
                '1.2.3'        # Too few octets
            ]
            
            for invalid_ip in invalid_ips:
                mock_response.text = invalid_ip
                
                with pytest.raises(ValueError, match="Invalid IP address format"):
                    get_public_ip()