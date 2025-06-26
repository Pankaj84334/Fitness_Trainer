from fastapi import FastAPI
app= FastAPI()
@app.post("/login")
def login(username: str, password: str):
    if username == "admin" and password == "password":
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid credentials"}, 401