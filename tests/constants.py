from pydantic import SecretStr

ENCODING_SECRET = SecretStr("1234567890abcdef")
HASH_SCHEMES = ["argon2"]
