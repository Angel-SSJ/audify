
class RoleSQLMapper(IMapper[RoleEntity, RoleModel]):
    def to_domain(self, model: RoleModel) -> RoleEntity:
        return RoleEntity(
            id=model.id,
            name=model.name,
            description=model.description,
            created_at=model.created_at,
            updated_at=model.updated_at,
            is_active=model.is_active
        )

    def to_persistence(self, entity: RoleEntity) -> RoleModel:
        return RoleModel(
            id=entity.id,
            name=entity.name,
            description=entity.description,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            is_active=entity.is_active
        )
