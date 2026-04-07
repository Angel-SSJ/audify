
class RoleUserSQLMapper(IMapper[RoleUserEntity, RoleUserModel]):
    def to_domain(self, model: RoleUserModel) -> RoleUserEntity:
        return RoleUserEntity(
            id=model.id,
            user_id=model.user_id,
            role_id=model.role_id,
            created_at=model.created_at,
            updated_at=model.updated_at,
            is_active=model.is_active
        )

    def to_persistence(self, entity: RoleUserEntity) -> RoleUserModel:
        return RoleUserModel(
            id=entity.id,
            user_id=entity.user_id,
            role_id=entity.role_id,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            is_active=entity.is_active
        )
