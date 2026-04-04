
def get_user_repository(
    db:AsyncIOMotorDatabase = Depends(get_database)
):

    return UserRepository(db)
