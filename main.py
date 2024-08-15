from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from dtos import UserCreate, UserUpdate, LinkCreate, DarajaCreate, DarajaUpdate, FriendCreate
from functions import create_user, update_user, create_link, delete_link, get_links, create_daraja, update_daraja, \
    delete_daraja, get_all_daraja, get_daraja, get_user_by_tg_id, get_user_by_id, create_friend
from models import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/create/user")
async def user_create(user: UserCreate, db: Session = Depends(get_db)):
    response = await create_user(user, db)
    return {"message": "user successfully created",
            "statusCode": 200,
            "data": response
            }


@app.put("/update/user")
async def user_update(user: UserUpdate, db: Session = Depends(get_db)):
    response = await update_user(user, db)
    return {"message": "user successfully updated",
            "statusCode": 200,
            "data": response
            }


@app.get("/get/user")
async def user_get(user_id: int, db: Session = Depends(get_db)):
    response = get_user_by_id(user_id, db)
    return {"message": "user successfully fetched",
            "statusCode": 200,
            "data": response
            }


@app.get("/get/tg_id/user")
async def get_tg_id(tg_id: int, db: Session = Depends(get_db)):
    response = await get_user_by_tg_id(tg_id, db)
    return {"message": "user successfully fetched by telegram id",
            "statusCode": 200,
            "data": response
            }


@app.post("/create/link")
async def link_create(link: LinkCreate, db: Session = Depends(get_db)):
    response = await create_link(link, db)
    return {"message": "link successfully created",
            "statusCode": 200,
            "data": response
            }


@app.delete("/delete/link")
async def link_delete(link_id: int, db: Session = Depends(get_db)):
    response = await delete_link(link_id, db)
    return {"message": "link successfully deleted",
            "statusCode": 200,
            "data": response
            }


@app.get("/get/link")
async def get_link(db: Session = Depends(get_db)):
    response = await get_links(db)
    return {"message": "fetched all links ",
            "statusCode": 200,
            "data": response
            }


@app.post("/create/daraja")
async def daraja_create(user: DarajaCreate, db: Session = Depends(get_db)):
    response = await create_daraja(user, db)
    return {"message": "Daraja successfully created",
            "statusCode": 200,
            "data": response
            }


@app.put("/update/daraja")
async def daraja_update(user: DarajaUpdate, db: Session = Depends(get_db)):
    response = await update_daraja(user, db)
    return {"message": "Daraja successfully updated",
            "statusCode": 200,
            "data": response
            }


@app.delete("/delete/daraja")
async def daraja_delete(daraja_id: int, db: Session = Depends(get_db)):
    response = await delete_daraja(daraja_id, db)
    return {"message": "Daraja successfully deleted",
            "statusCode": 200,
            "data": response
            }


@app.get("/get/all/daraja")
async def get_total_daraja(db: Session = Depends(get_db)):
    response = await get_all_daraja(db)
    return {"message": "Fetched all daraja",
            "statusCode": 200,
            "data": response
            }


@app.get("/get/daraja")
async def take_daraja(daraja_id: int, db: Session = Depends(get_db)):
    response = await get_daraja(daraja_id, db)
    return {"message": "Fetched daraja successfully",
            "statusCode": 200,
            "data": response
            }


@app.post("/create/friend")
async def friend_create(user: FriendCreate, db: Session = Depends(get_db)):
    response = await create_friend(user, db)
    return {"message": "Fetched daraja successfully",
            "statusCode": 200,
            "data": response
            }
