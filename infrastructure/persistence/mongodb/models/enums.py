from enum import Enum

class AudioStreamingQuality(str, Enum):
    low = 'low'
    normal = 'normal'
    high = 'high'


class DownloadQuality(str, Enum):
    low = 'low'
    normal = 'normal'
    high = 'high'


class LanguageEnum(str, Enum):
    english = 'english'
    spanish = 'spanish'


class MusicalGenre(str, Enum):
    pop = "pop"
    reggaeton = "reggaeton"
    rock = "rock"
    jazz = "jazz"
    trap_latino = "trap latino"
    salsa = "salsa"
    bachata = "bachata"
    merengue = "merengue"
    cumbia = "cumbia"
    balada = "balada"
    ranchera = "ranchera"
    regional_mexicano = "regional mexicano"
    trap_argentino = "trap argentino"
    classical = "classical"
    electronic = "electronic"
    hip_hop = "hip hop"

class VideoStreamingQualityResolution(str, Enum):
    ultra_high = '1080p'
    high = '720p'
    normal = '480p'
    low = '360p'

class ArtistRole(str, Enum):
    primary = 'primary'
    featured = 'featured'


class VideoStreamingQuality(str, Enum):
    low = 'low'
    normal = 'normal'
    high = 'high'

class AccountType(str, Enum):
    free = 'free'
    premium = 'premium'

class PlaybackContextType(str, Enum):
    playlist = 'playlist'
    album = 'album'
    artist = 'artist'
    search_result = 'search_result'

class ReleaseType(str, Enum):
    album = 'album'
    ep = 'ep'
    single = 'single'
