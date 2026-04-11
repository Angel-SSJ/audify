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
    def to_persistence(domain_entity: any) -> dict:
        if hasattr(domain_entity, "model_dump"):
            data = domain_entity.model_dump(exclude={"id"},exclude_unset=True)
        elif hasattr(domain_entity, "copy"):
            data = domain_entity.copy()
        else:
            data = dict(domain_entity)

        entity_id = getattr(domain_entity, "id", None)
        if entity_id:
            data["_id"] = ObjectID(entity_id)

        return data
