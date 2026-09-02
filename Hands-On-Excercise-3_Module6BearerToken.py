from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Security, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import uvicorn

app = FastAPI()
security = HTTPBearer()

# Define expected JSON body data
class Item(BaseModel):
    name: str
    description: str | None = None
    
# Simple mock verification function
def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)) -> str:
    token = ""
    with open("Hands-On-Excercise-3_Module6SecretKey.txt", "r", encoding="utf-8") as f:
        token = f.readline()
    print(token)
    # Replace this with your actual token validation logic (e.g., JWT decode)
    if token != "my-secret-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token

@app.post("/submit/")
async def create_item_and_write(
    item: Item, 
    token: Annotated[str, Depends(verify_token)]
):
    # Write the received data to a local text file    
    with open("output.txt", "a", encoding="utf-8") as f:
        f.write(f"Token Used: {token}\nData: {item.model_dump_json()}\n---\n")
        
    return {
        "status": "success", 
        "message": "Data written to file successfully", 
        "received": item
    }
    
if __name__ == "__main__":
    # Start the server programmatically
    uvicorn.run("Hands-On-Excercise-3_Module6BearerToken:app", host="127.0.0.1", port=9006, reload=True)