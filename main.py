import requests
import hashlib

def check_breach(password):
    # Hash the password using SHA-1 algorithm
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    # Make an API request to check if the password has been breached
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    # Check if the password hash suffix exists in the response

    # The API works by receiving the first five characters of the SHA-1 hash algorithm of a password
    # It returns a list of hashes that match those initial characters.
    if response.status_code == 200:
        # Status code 200 indicates a successful request
        hashes = response.text.splitlines()
        for hash in hashes:
            if hash.startswith(suffix):
                count = int(hash.split(':')[1])
                if count > 0:
                    return f"Your password has been breached {count} time(s). It is recommended to change your password immediately!"
        # If the loop completes without finding any breaches, return a non-breached message
        return "Your password has not been breached."
    else:
        # Handle the error
        return "Error occurred while checking the breach status."