from pympler.asizeof import asizeof

users: list[str] = ["john", "marry", "mark", "jack", "marry", "mark"]

# users_seen = set()
# for user in users:
#     if user in users_seen:
#         continue
#     users_seen.add(user)
#     print(user)


def dedup(collection):
    items = set()
    for item in collection:
        if item in items:
            continue
        items.add(item)
        yield item


for user in dedup(users):
    print(user)

print(asizeof(users))
