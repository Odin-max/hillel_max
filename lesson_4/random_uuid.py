from typing import Generator
from uuid import UUID, uuid4

used_uuids_by_user: dict[str, set[UUID]] = {}


def generate_unique_uuid_as_function(user: str) -> UUID:
    while True:
        generated_uuid = uuid4()

        if generated_uuid not in used_uuids_by_user[user]:
            used_uuids_by_user[user].add(generated_uuid)
            return generated_uuid


def generate_unique_uuid() -> Generator[UUID, None, None]:
    used_uuids: set[UUID] = set()
    while True:
        generated_uuid = uuid4()

        if generated_uuid not in used_uuids:
            used_uuids.add(generated_uuid)
            yield generated_uuid


john_unique_uuid = generate_unique_uuid()
marry_unique_uuid = generate_unique_uuid()

print(next(john_unique_uuid))
print(next(john_unique_uuid))
print(next(marry_unique_uuid))
print(next(marry_unique_uuid))
