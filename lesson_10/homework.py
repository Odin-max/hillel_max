import time
from abc import ABC, abstractmethod


class SocialChannel(ABC):
    def __init__(self, followers: int, name: str):
        self.followers: int = followers
        self.name: str = name

    @abstractmethod
    def post(self, message: str):
        ...


class Post:
    def __init__(self, message, timestamp):
        self.message = message
        self.timestamp = timestamp

    def __iter__(self):
        yield self.message
        yield self.timestamp


class Youtube(SocialChannel):
    def post(self, message: str):
        print(f"Posting to Youtube: {message}")


class Facebook(SocialChannel):
    def post(self, message: str):
        print(f"Posting to Facebook: {message}")


class Twitter(SocialChannel):
    def post(self, message: str):
        print(f"Posting to Twitter: {message}")


def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    for post in posts:
        message, timestamp = post.message, post.timestamp
        for channel in channels:
            if (
                timestamp <= time.time()
                and channel.name.lower() in message.lower()
            ):
                channel.post(message)


youtube = Youtube(100000, "YouTube")
facebook = Facebook(50000, "Facebook")
twitter = Twitter(20000, "Twitter")

channels = [youtube, facebook, twitter]

posts = [
    Post("Message YouTube!", 1),
    Post("Message Facebook!", 2),
    Post("Message Twitter!", 3),
]

process_schedule(posts, channels)
