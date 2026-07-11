from passlib.context import CryptContext  # type: ignore[import]

# bcrypt is preferred because it is slow and protects
# against brute-force attacks unlike MD5 or SHA-256.

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )