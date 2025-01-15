from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from dtos import UserUpdate, LinkCreate, DarajaCreate, DarajaUpdate
from functions import create_user, update_user, create_link, delete_link, get_links, create_daraja, update_daraja, \
    delete_daraja, get_all_daraja, get_daraja, get_user_by_tg_id, get_user_by_id, create_friend, my_friend, delete_user, \
    delete_all_links, get_top_users, delete_all_users, delete_friend, my_daraja
from models import SessionLocal

app = FastAPI(
    docs_url="/can-do-crash-me",  # Disables Swagger UI at /docs
    redoc_url=None, # Disables ReDoc UI at /redoc
    openapi_url="/openapi.json" # Disables OpenAPI schema at /openapi.json
    )

origins = [
    # "https://uzfiesta.uz",
    # "https://takbir-web-app.vercel.app/"
    "*"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Add Trusted Host middleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["uzfiesta.uz", "api.alehson.uz", "takbir-web-app.vercel.app"],
)

# Add HTTPS Redirect middleware
# app.add_middleware(HTTPSRedirectMiddleware)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/for/test")
async def root():
    return {"message": "Good morning!"}


@app.post("/create/user")
async def user_create(full_name: str, tg_id: int, db: Session = Depends(get_db)):
    response = await create_user(full_name, tg_id, db)
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


@app.delete("/delete/user")
async def user_delete(tg_id: int, db: Session = Depends(get_db)):
    response = await delete_user(tg_id, db)
    return {"message": "user successfully deleted",
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


@app.get("/get/top/user")
async def top_users(db: Session = Depends(get_db)):
    response = await get_top_users(db)
    return {"message": "user successfully fetched",
            "statusCode": 200,
            "data": response
            }


@app.get("/get/all/id/user")
async def get_all_id(db: Session = Depends(get_db)):
    response = await get_all_user_only_id(db)
    return {"message": "user's id successfully fetched",
            "statusCode": 200,
            "data": response
            }

@app.delete("/delete/all/users")
async def all_user_delete(db: Session = Depends(get_db)):
    response = await delete_all_users(db)
    return {"message": "all user successfully deleted",
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


@app.delete("/delete-all/link")
async def delete_all_link(db: Session = Depends(get_db)):
    response = await delete_all_links(db)
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


@app.get("/get/my/daraja")
async def get_my_daraja(total_count: int, db: Session = Depends(get_db)):
    response = await my_daraja(total_count, db)
    return {"message": "your daraja successfully fetched",
            "statusCode": 200,
            "data": response
            }


@app.post("/create/friend")
async def friend_create(user_id: int, friend_tg_id: int, db: Session = Depends(get_db)):
    response = await create_friend(user_id, friend_tg_id, db)
    return {"message": "Successfully created friend",
            "statusCode": 200,
            "data": response
            }


@app.get("/get-all/friends")
async def all_friends(my_tg_id: int, db: Session = Depends(get_db)):
    response = await my_friend(my_tg_id, db)
    return {"message": "Fetched friends successfully",
            "statusCode": 200,
            "data": response
            }


@app.delete("/delete-all/friends")
async def delete_all_friend(db: Session = Depends(get_db)):
    response = await delete_friend(db)
    return {"message": "all friends successfully deleted",
            "statusCode": 200,
            "data": response
            }
