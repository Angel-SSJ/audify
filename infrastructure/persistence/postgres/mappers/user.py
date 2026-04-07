from domain.entities.user import UserEntity
from infrastructure.persistence.postgres.models.user.model import UserModel
from domain.interfaces.mapper import IMapper

class UserSQLMapper(IMapper[UserEntity, UserModel]):
    @staticmethod
    def to_domain(persistence_model: UserModel) -> UserEntity:
        if not persistence_model:
            return None
        return UserEntity(
            id=persistence_model.id,
            first_name=persistence_model.first_name,
            last_name=persistence_model.last_name,
            user_name=persistence_model.username,
            email=persistence_model.email,
            hashed_password=persistence_model.hashed_password,
            role=persistence_model.role,
            account_type=None, # Update if needed
            is_active=persistence_model.is_active
        )

    @staticmethod
    def to_persistence(domain_entity: UserEntity) -> dict:
        return {
            "id": domain_entity.id,
            "first_name": domain_entity.first_name,
            "last_name": domain_entity.last_name,
            "username": domain_entity.user_name,
            "email": domain_entity.email,
            "hashed_password": domain_entity.hashed_password,
            "role": domain_entity.role,
            "is_active": domain_entity.is_active
        }
