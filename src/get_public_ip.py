import requests
import re

def get_public_ip() -> str:
    """
    Retrieve the public IP address of the system.

    Returns:
        str: The public IP address of the system.

    Raises:
        ConnectionError: If unable to connect to IP lookup service.
        ValueError: If no valid IP address is found.
    """
    try:
        # Use a reliable IP lookup service
        response = requests.get('https://api.ipify.org', timeout=10)
        
        # Validate the response
        if response.status_code != 200:
            raise ConnectionError(f"Failed to retrieve public IP. Status code: {response.status_code}")
        
        # Strip any whitespace
        ip_address = response.text.strip()
        
        # Use a more robust IP validation regex
        ip_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
        if not ip_pattern.match(ip_address):
            raise ValueError(f"Invalid IP address format: {ip_address}")
        
        # Additional numeric validation for each octet
        octets = ip_address.split('.')
        for octet in octets:
            octet_value = int(octet)
            if octet_value < 0 or octet_value > 255:
                raise ValueError(f"IP octet out of range: {octet}")
        
        return ip_address
    
    except requests.RequestException as e:
        raise ConnectionError(f"Network error when retrieving IP: {e}")
    except (ValueError, TypeError) as e:
        raise ValueError(f"IP validation error: {e}")