from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import uvicorn

app = FastAPI(title="Bearer Token API Server")

# Initialize the HTTPBearer security scheme
security = HTTPBearer()

# Define a secure token (In production, load this from an environment variable)
VALID_BEARER_TOKEN = "my-secret-token"

def validate_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Dependency function that extracts the Bearer token from the
    Authorization header and validates it.
    """
    token = credentials.credentials
    if token != VALID_BEARER_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing Bearer Token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token

@app.get("/api/public")
def public_endpoint():
    """An open endpoint that anyone can access without a token."""
    return {"message": "Welcome! This endpoint is public and does not require authentication."}

@app.get("/api/protected")
def protected_endpoint(token: str = Depends(validate_token)):
    """A secure endpoint that requires a valid Bearer token."""
    return {
        "message": "Access granted! You have successfully reached the protected route.",
        "authenticated_with": f"Bearer {token[:3]}..."
    }

if __name__ == "__main__":
    # Run the server locally on port 8005
    uvicorn.run("BearerToken:app", host="127.0.0.1", port=8005, reload=True)