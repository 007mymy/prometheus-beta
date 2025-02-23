import requests
import re
from typing import Optional

def get_public_ip(timeout: Optional[int] = 10) -> str:
    """
    Retrieve the public IP address of the system.

    Args:
        timeout (int, optional): Timeout for the HTTP request in seconds. Defaults to 10.

    Returns:
        str: The public IP address of the system.

    Raises:
        ConnectionError: If unable to connect to IP lookup service.
        ValueError: If no valid IP address is found.
    """
    try:
        # Use a reliable IP lookup service
        response = requests.get('https://api.ipify.org', timeout=timeout)
        
        # Validate the response
        if response.status_code != 200:
            raise ConnectionError(f"Failed to retrieve public IP. Status code: {response.status_code}")
        
        # Strip any whitespace
        ip_address = response.text.strip()
        
        # Validate IP format and octets
        if not _is_valid_ip(ip_address):
            raise ValueError("Invalid IP address format")
        
        return ip_address
    
    except requests.RequestException as e:
        raise ConnectionError(f"Network error when retrieving IP: {e}")

def _is_valid_ip(ip_address: str) -> bool:
    """
    Validate the format and values of an IP address.

    Args:
        ip_address (str): IP address to validate.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    # Use a more robust IP validation regex
    ip_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    if not ip_pattern.match(ip_address):
        return False
    
    # Additional numeric validation for each octet
    octets = ip_address.split('.')
    if len(octets) != 4:
        return False
    
    try:
        for octet in octets:
            octet_value = int(octet)
            if octet_value < 0 or octet_value > 255:
                return False
    except (ValueError, TypeError):
        return False
    
    return True