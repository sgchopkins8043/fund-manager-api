from fastapi import APIRouter

router = APIRouter(prefix='/api/funds', tags=['funds'])

@router.get("/all")
async def get_all_funds():
    return {"message": "All funds provided"}


