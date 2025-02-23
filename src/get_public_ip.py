import requests

def get_public_ip():
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
            raise ConnectionError("Failed to retrieve public IP")
        
        # Strip any whitespace and validate IP format
        ip_address = response.text.strip()
        
        # Basic IP address validation
        parts = ip_address.split('.')
        if len(parts) != 4:
            raise ValueError("Invalid IP address format")
        
        for part in parts:
            if not part.isdigit() or not (0 <= int(part) <= 255):
                raise ValueError("Invalid IP address format")
        
        return ip_address
    
    except requests.RequestException as e:
        raise ConnectionError(f"Network error when retrieving IP: {e}")