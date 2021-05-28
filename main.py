from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def index():
    return {"data": "list of tenants"}

@app.get("/tenant/{tenant_id}")
def tenant(tenant_id: int):
    return {"data": {id: tenant_id, ir: tenant_idx }}

@app.get("/tenant/{tenant_id}/details")
def get_tenant_details(tenant_id):
    return {"data": "details"}

class Contact(BaseModel):
    contact_id:int
    first_name:str
    last_name:str
    user_name:str
    password:str
@app.post('/contact')
async def create_contact(contact: Contact):
    return contact
