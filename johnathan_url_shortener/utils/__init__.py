import random
import string


def generate_token() -> str:
    """This method generates a random token with 8 characters."""
    
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(8)
    )
