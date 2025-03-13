import sys
import os

print(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
# Dynamically add the project root to the Python module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from fastapi import Request, HTTPException
from shared.firebase_auth import validate_token

async def authenticate(request: Request):
    """
    Dependency for authenticating Firebase tokens.
    """
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid or missing token")

    token = auth_header.split(" ")[1]  # Extract the token from the header
    return validate_token(token)  # Validate the token and return the user data