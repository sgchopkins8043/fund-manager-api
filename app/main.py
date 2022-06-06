from fastapi import FastAPI
from routers import router_funds
from routers import router_transactions

app = FastAPI()
app.include_router(router_funds.router)
app.include_router(router_transactions.router)


