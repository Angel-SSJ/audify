-- Tablas base
CREATE TABLE IF NOT EXISTS users (
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL UNIQUE,
    hashed_password VARCHAR(255) NOT NULL,
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at TIMESTAMPTZ DEFAULT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS roles (
    name VARCHAR(255) NOT NULL UNIQUE,
    description VARCHAR(255) NOT NULL,
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at TIMESTAMPTZ DEFAULT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS user_roles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL,
    role_id UUID NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at TIMESTAMPTZ DEFAULT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE CASCADE,
    UNIQUE (user_id, role_id)
);

-- Roles iniciales
INSERT INTO roles (name, description)
VALUES
    ('admin', 'Administrador del sistema'),
    ('user', 'Usuario del sistema'),
    ('artist', 'Artista')
ON CONFLICT (name) DO NOTHING;

-- Función corregida
CREATE OR REPLACE FUNCTION create_user_roles(
    role_name TEXT,
    email_user TEXT
)
RETURNS VOID AS $$
DECLARE
    u_id UUID;
    r_id UUID;
BEGIN
    SELECT id INTO u_id FROM users WHERE email = email_user;
    SELECT id INTO r_id FROM roles WHERE name = role_name;

    IF u_id IS NOT NULL AND r_id IS NOT NULL THEN
        INSERT INTO user_roles (user_id, role_id)
        VALUES (u_id, r_id)
        ON CONFLICT (user_id, role_id) DO NOTHING;
    END IF;
END;
$$ LANGUAGE plpgsql;

-- Usuarios de prueba
INSERT INTO users (email, hashed_password, first_name, last_name, username)
VALUES ('admin@gmail.com', encode(digest('admin@123', 'sha256'), 'hex'), 'Admin', 'Admin', 'admin')
ON CONFLICT (email) DO NOTHING;

INSERT INTO users (email, hashed_password, first_name, last_name, username)
VALUES ('angel@gmail.com', encode(digest('angel@123', 'sha256'), 'hex'), 'Angel', 'Ramirez', 'angel_ssj')
ON CONFLICT (email) DO NOTHING;

-- Asignar roles
SELECT create_user_roles('admin', 'admin@gmail.com');
SELECT create_user_roles('user', 'angel@gmail.com');
