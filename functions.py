from fastapi import HTTPException
from models import *
from dtos import *


async def create_user(full_name: str, tg_id: int, db):
    db_user = db.query(User).filter(User.tg_id == tg_id).first()
    if db_user is not None:
        raise HTTPException(status_code=409, detail="User already exists")

    user1 = User(
        tg_id=tg_id,
        full_name=full_name,
        total_count=0,
        total_coin=0,
        channels="",
        share_link=f"https://t.me/Istigfar_bot/Savob?startapp={tg_id}"
    )
    db.add(user1)
    db.commit()
    db.refresh(user1)
    return UserResult(
        full_name=user1.full_name,
        total_count=user1.total_count,
        total_coin=user1.total_coin,
        channels=user1.channels,
        share_link=user1.share_link
    )


async def update_user(user: UserUpdate, db):
    db_user = db.query(User).filter(User.tg_id == user.id).first()

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    if user.full_name is not None:
        db_user.full_name = user.full_name
    if user.total_count is not None:
        db_user.total_count = user.total_count
    if user.total_coin is not None:
        db_user.total_coin = user.total_coin
    if user.channels is not None:
        db_user.channels = user.channels

    db.commit()
    db.refresh(db_user)
    return UserResult(
        full_name=db_user.full_name,
        total_count=db_user.total_count,
        total_coin=db_user.total_coin,
        channels=db_user.channels,
        share_link=db_user.share_link
    )


async def delete_user(tg_id: int, db):
    db_user = db.query(User).filter(User.tg_id == tg_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(db_user)
    db.commit()
    # db.refresh(db_user)
    return True


async def get_user_by_tg_id(tg_id: int, db):
    db_user = db.query(User).filter(User.tg_id == tg_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResult(
        full_name=db_user.full_name,
        total_count=db_user.total_count,
        total_coin=db_user.total_coin,
        channels=db_user.channels,
        share_link=db_user.share_link
    )


async def get_user_by_id(user_id: int, db):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResult(
        full_name=db_user.full_name,
        total_count=db_user.total_count,
        share_link=db_user.share_link
    )


async def get_top_users(db):
    top_users = db.query(User).order_by(User.id.desc()).all()
    top_user = []
    for user in top_users:
        user1 = UserResult(
            full_name=user.full_name,
            total_count=user.total_count,
            total_coin=user.total_coin,
            channels=user.channels,
            share_link=user.share_link
        )
        top_user.append(user1)

    return top_user


async def get_all_user_only_id(db):
    db_users = db.query(User).all()
    ids = []
    for user in db_users:
        id = user.tg_id
        ids.append(id)
        
    return ids


async def delete_all_users(db):
    all_users = db.query(User).all()
    for user in all_users:
        db.delete(user)
        db.commit()

    return True


async def create_link(link: LinkCreate, db):
    link_one = Link(
        name=link.name,
        url=link.url,
        chat_id=link.chat_id
    )
    db.add(link_one)
    db.commit()
    db.refresh(link_one)
    return True


async def delete_link(link_id: int, db):
    link = db.query(Link).filter(Link.id == link_id).first()
    if link is None:
        raise HTTPException(status_code=404, detail="Link not found")

    db.delete(link)
    db.commit()
    return True


async def delete_all_links(db):
    links = db.query(Link).all()
    for link in links:
        db.delete(link)
        db.commit()

    return True


async def get_links(db):
    links = db.query(Link).all()
    links2 = []
    for link in links:
        link_link = LinkResult(
            name=link.name,
            url=link.url,
            chat_id=link.chat_id
        )
        links2.append(link_link)

    return links2


async def create_daraja(daraja: DarajaCreate, db):
    db_daraja = db.query(Daraja).filter(Daraja.daraja == daraja.daraja).first()
    if db_daraja is not None:
        raise HTTPException(status_code=402, detail="Daraja already exists")
    new_daraja = Daraja(
        name=daraja.name,
        daraja=daraja.daraja,
        started_at=daraja.started_at,
        limit=daraja.limit
    )

    db.add(new_daraja)
    db.commit()
    db.refresh(new_daraja)
    return DarajaResult(
        name=new_daraja.name,
        daraja=new_daraja.daraja,
        started_at=new_daraja.started_at,
        limit=new_daraja.limit
    )


async def update_daraja(daraja: DarajaUpdate, db):
    db_daraja = db.query(Daraja).filter(Daraja.id == daraja.id).first()
    if db_daraja is None:
        raise HTTPException(status_code=404, detail="Daraja not found")

    if daraja.name is not None:
        db_daraja.name = daraja.name
    if daraja.started_at is not None:
        db_daraja.started_at = daraja.started_at
    if daraja.limit is not None:
        db_daraja.limit = daraja.limit

    db.commit()
    db.refresh(db_daraja)
    return DarajaResult(
        name=daraja.name,
        daraja=db_daraja.daraja,
        started_at=daraja.started_at,
        limit=daraja.limit
    )


async def delete_daraja(daraja_id: int, db):
    db_daraja = db.query(Daraja).filter(Daraja.id == daraja_id).first()
    if db_daraja is None:
        raise HTTPException(status_code=404, detail="Daraja not found")

    db.delete(db_daraja)
    db.commit()
    db.refresh(db_daraja)
    return True


async def get_all_daraja(db):
    db_daraja = db.query(Daraja).all()
    daraja_all = list()
    for daraja in db_daraja:
        da_raja = DarajaResult(
            name=daraja.name,
            daraja=daraja.daraja,
            started_at=daraja.started_at,
            limit=daraja.limit
        )
        daraja_all.append(da_raja)

    return daraja_all


async def get_daraja(daraja_id: int, db):
    db_daraja = db.query(Daraja).filter(Daraja.id == daraja_id).first()
    if db_daraja is None:
        raise HTTPException(status_code=404, detail="Daraja not found")
    return DarajaResult(
        name=db_daraja.name,
        daraja=db_daraja.daraja,
        started_at=db_daraja.started_at,
        limit=db_daraja.limit
    )


async def create_friend(user_id: int, friend_tg_id: int, db):
    user = db.query(User).filter(User.tg_id == friend_tg_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Friend not found")

    db_friend = db.query(Friend).filter(Friend.friend_tg_id == friend_tg_id).first()
    if db_friend is not None:
        raise HTTPException(status_code=403, detail="Friend already exists")

    new_friend = Friend(
        user_id=user_id,
        friend_tg_id=friend_tg_id
    )
    db.add(new_friend)
    db.commit()
    db.refresh(new_friend)
    return True


async def my_friend(my_tg_id: int, db):
    db_user = db.query(User).filter(User.tg_id == my_tg_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db_friend = db.query(Friend).filter(Friend.user_id == my_tg_id)
    if db_friend is None:
        raise HTTPException(status_code=404, detail="Friend not found")
    data = list()
    for friend in db_friend:
        my_fr = db.query(User).filter(User.tg_id == friend.friend_tg_id).first()
        if my_fr is not None:
            daraja_my = await my_daraja(my_fr.total_count, db)
            salom = FriendResult(
                full_name=my_fr.full_name,
                daraja=daraja_my,
                total_count=my_fr.total_count
            )
            data.append(salom)

    return data


async def delete_friend(db):
    friends = db.query(Friend).all()
    for friend in friends:
        db.delete(friend)
        db.commit()

    return True


async def my_daraja(total_count: int, db):
    db_daraja = db.query(Daraja).all()
    user_daraja = 0
    for daraja in db_daraja:
        if daraja.started_at <= total_count:
            user_daraja = daraja.daraja
        else:
            break

    return user_daraja
