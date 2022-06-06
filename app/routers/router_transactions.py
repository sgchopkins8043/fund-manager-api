from fastapi import APIRouter

router = APIRouter(prefix='/api/transactions', tags=['transactions'])

@router.get("/all")
async def get_all_transactions():
    return {"message": "All transactions provided"}