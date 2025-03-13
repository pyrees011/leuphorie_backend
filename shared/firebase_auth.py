import os
import firebase_admin
from firebase_admin import credentials, auth
from fastapi import HTTPException

# Initialize Firebase Admin SDK (singleton pattern to avoid reinitialization)
if not firebase_admin._apps:
    cred_path = os.getenv("FIREBASE_CRED_PATH", "../../shared/firebase_cred.json")  # Use env var or default path
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

def validate_token(token: str):
    """
    Validates the Firebase token and returns the decoded token.
    Raises an HTTPException if the token is invalid or expired.
    """
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token  # Decoded token contains user info (e.g., uid, email)
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
