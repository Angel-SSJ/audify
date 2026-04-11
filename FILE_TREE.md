# File Tree: audify

```
├── 📁 api
│   ├── 📁 controllers
│   │   ├── 🐍 __init__.py
│   │   ├── 🐍 albums.py
│   │   ├── 🐍 artists.py
│   │   ├── 🐍 auth.py
│   │   ├── 🐍 playback_history.py
│   │   ├── 🐍 playlists.py
│   │   ├── 🐍 tracks.py
│   │   └── 🐍 users.py
│   ├── 📁 dependencies
│   │   ├── 🐍 __init__.py
│   │   ├── 🐍 album_dependency.py
│   │   ├── 🐍 artist_dependency.py
│   │   ├── 🐍 auth_dependency.py
│   │   ├── 🐍 playback_history_dependency.py
│   │   ├── 🐍 playlist_dependency.py
│   │   ├── 🐍 track_dependency.py
│   │   └── 🐍 user_dependency.py
│   ├── 📁 dtos
│   │   ├── 🐍 albums.py
│   │   ├── 🐍 artists.py
│   │   ├── 🐍 auth.py
│   │   ├── 🐍 playback_history.py
│   │   ├── 🐍 playlist.py
│   │   ├── 🐍 tracks.py
│   │   └── 🐍 users.py
│   ├── 📁 helpers
│   │   ├── 🐍 object_id.py
│   │   ├── 🐍 pagination.py
│   │   └── 🐍 query_params.py
│   ├── 🐍 __init__.py
│   ├── 🐍 config.py
│   └── 🐍 main.py
├── 📁 app
│   └── 📁 controllers
├── 📁 application
│   ├── 📁 services
│   │   ├── 🐍 __init__.py
│   │   ├── 🐍 albums.py
│   │   ├── 🐍 artists.py
│   │   ├── 🐍 authentication.py
│   │   ├── 🐍 base.py
│   │   ├── 🐍 playback_history.py
│   │   ├── 🐍 playlists.py
│   │   ├── 🐍 tracks.py
│   │   └── 🐍 users.py
│   └── 🐍 __init__.py
├── 📁 domain
│   ├── 📁 abstractions
│   │   ├── 🐍 __init__.py
│   │   ├── 🐍 base.py
│   │   └── 🐍 enums.py
│   ├── 📁 entities
│   │   ├── 🐍 __init__.py
│   │   ├── 🐍 album.py
│   │   ├── 🐍 artist.py
│   │   ├── 🐍 playback_history.py
│   │   ├── 🐍 playlist.py
│   │   ├── 🐍 role.py
│   │   ├── 🐍 role_user.py
│   │   ├── 🐍 track.py
│   │   └── 🐍 user.py
│   ├── 📁 exceptions
│   │   ├── 🐍 base.py
│   │   └── 🐍 user.py
│   ├── 📁 interfaces
│   │   ├── 🐍 __init__.py
│   │   ├── 🐍 authentication.py
│   │   ├── 🐍 mapper.py
│   │   ├── 🐍 repositories.py
│   │   └── 🐍 services.py
│   ├── 📁 object_values
│   │   ├── 🐍 __init__.py
│   │   ├── 🐍 account_type.py
│   │   ├── 🐍 aliases_artist.py
│   │   ├── 🐍 artist_embedded_track.py
│   │   ├── 🐍 artist_embeddings.py
│   │   ├── 🐍 images_profile_artists.py
│   │   ├── 🐍 media_quality.py
│   │   ├── 🐍 metrics_artist.py
│   │   ├── 🐍 notification.py
│   │   ├── 🐍 playback_context.py
│   │   ├── 🐍 playback_device.py
│   │   ├── 🐍 playback_interactions.py
│   │   ├── 🐍 setting.py
│   │   ├── 🐍 social_links_artist.py
│   │   ├── 🐍 track_embeddings.py
│   │   └── 🐍 video_assets.py
│   └── 🐍 __init__.py
├── 📁 infrastructure
│   ├── 📁 persistence
│   │   ├── 📁 mongodb
│   │   │   ├── 📁 mappers
│   │   │   │   ├── 🐍 __init__.py
│   │   │   │   ├── 🐍 album.py
│   │   │   │   ├── 🐍 artist.py
│   │   │   │   ├── 🐍 playback_history.py
│   │   │   │   ├── 🐍 playlist.py
│   │   │   │   ├── 🐍 track.py
│   │   │   │   └── 🐍 user.py
│   │   │   ├── 📁 models
│   │   │   │   ├── 📁 abstractions
│   │   │   │   │   ├── 🐍 __init__.py
│   │   │   │   │   └── 🐍 base.py
│   │   │   │   ├── 📁 album
│   │   │   │   │   ├── 🐍 __init__.py
│   │   │   │   │   └── 🐍 model.py
│   │   │   │   ├── 📁 artist
│   │   │   │   │   ├── 🐍 __init__.py
│   │   │   │   │   ├── 🐍 model.py
│   │   │   │   │   └── 🐍 schemas.py
│   │   │   │   ├── 📁 device
│   │   │   │   │   └── 🐍 schemas.py
│   │   │   │   ├── 📁 media
│   │   │   │   │   └── 🐍 schemas.py
│   │   │   │   ├── 📁 metrics
│   │   │   │   │   └── 🐍 schemas.py
│   │   │   │   ├── 📁 notification
│   │   │   │   │   └── 🐍 schemas.py
│   │   │   │   ├── 📁 playback_history
│   │   │   │   │   ├── 🐍 __init__.py
│   │   │   │   │   ├── 🐍 model.py
│   │   │   │   │   └── 🐍 schemas.py
│   │   │   │   ├── 📁 playlist
│   │   │   │   │   ├── 🐍 __init__.py
│   │   │   │   │   └── 🐍 model.py
│   │   │   │   ├── 📁 social
│   │   │   │   │   └── 🐍 schemas.py
│   │   │   │   ├── 📁 track
│   │   │   │   │   ├── 🐍 __init__.py
│   │   │   │   │   ├── 🐍 model.py
│   │   │   │   │   └── 🐍 schemas.py
│   │   │   │   ├── 📁 user
│   │   │   │   │   ├── 🐍 __init__.py
│   │   │   │   │   ├── 🐍 model.py
│   │   │   │   │   └── 🐍 schemas.py
│   │   │   │   ├── 🐍 __init__.py
│   │   │   │   └── 🐍 enums.py
│   │   │   ├── 📁 repositories
│   │   │   │   ├── 🐍 __init__.py
│   │   │   │   ├── 🐍 albums.py
│   │   │   │   ├── 🐍 artists.py
│   │   │   │   ├── 🐍 base.py
│   │   │   │   ├── 🐍 playbacks_history.py
│   │   │   │   ├── 🐍 playlists.py
│   │   │   │   ├── 🐍 tracks.py
│   │   │   │   └── 🐍 users.py
│   │   │   ├── 🐍 __init__.py
│   │   │   └── 🐍 mongo.py
│   │   ├── 📁 postgres
│   │   │   ├── 📁 mappers
│   │   │   │   ├── 🐍 role.py
│   │   │   │   ├── 🐍 role_user.py
│   │   │   │   └── 🐍 user.py
│   │   │   ├── 📁 models
│   │   │   │   ├── 📁 role
│   │   │   │   │   └── 🐍 model.py
│   │   │   │   ├── 📁 role_user
│   │   │   │   │   └── 🐍 model.py
│   │   │   │   ├── 📁 user
│   │   │   │   │   ├── 🐍 model.py
│   │   │   │   │   └── 🐍 schemas.py
│   │   │   │   └── 🐍 base.py
│   │   │   ├── 📁 repositories
│   │   │   │   ├── 🐍 base.py
│   │   │   │   ├── 🐍 role.py
│   │   │   │   ├── 🐍 role_user.py
│   │   │   │   └── 🐍 user.py
│   │   │   ├── 📁 scripts
│   │   │   │   ├── 📄 audify.sql
│   │   │   │   └── 🐍 run_init_sql.py
│   │   │   └── 🐍 postgres.py
│   │   └── 🐍 __init__.py
│   ├── 📁 security
│   │   └── 🐍 jwt_service.py
│   └── 🐍 __init__.py
├── ⚙️ .gitignore
├── 📝 README.md
└── ⚙️ pyproject.toml
```
