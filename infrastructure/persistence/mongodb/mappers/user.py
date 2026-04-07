from domain.entities.user import UserEntity
from infrastructure.persistence.mongodb.models.user.model import User
from domain.interfaces.mapper import IMapper
from api.helpers.object_id import ObjectID

class UserMapper(IMapper[UserEntity, User]):
    @staticmethod
    def to_domain(persistence_model: User) -> UserEntity:
        return UserEntity(
            id=str(persistence_model.id),
            first_name=persistence_model.first_name,
            last_name=persistence_model.last_name,
            user_name=persistence_model.user_name,
            email=persistence_model.email,
            account_type=persistence_model.account_type.value if persistence_model.account_type else None,
            settings=persistence_model.settings.model_dump() if persistence_model.settings else None,
            is_active=persistence_model.is_active
        )

    @staticmethod
    def to_persistence(domain_entity: UserEntity) -> dict:
        data = domain_entity.model_dump(exclude={"id"})
        if domain_entity.id:
            data["_id"] = ObjectID(domain_entity.id)
        return data
