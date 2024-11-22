from dataclasses import dataclass


def link(text: str, url: str) -> str:
    return f'<a class="link" href="{url}">{text}</a>'


def award(text: str) -> str:
    return f'<span style="color: gold;">🏆 {text}</span>'


@dataclass(frozen=True)
class Head:
    title: str
    author: str = "Rocky Xu"
    description: str = ""
    keywords: str = ""


@dataclass(frozen=True)
class Bio:
    title: str
    image: str
    paragraphs: list[str]
    contacts: list[str]


@dataclass(frozen=True)
class Post:
    date: str
    description: str


@dataclass(frozen=True)
class Moments:
    title: str
    posts: list[Post]


@dataclass(frozen=True)
class Tag:
    name: str
    color: str
    logo: str = None


@dataclass(frozen=True)
class Item:
    image: str
    name: str
    tags: list[Tag] = None
    links: list[str] = None
    description: str = ""
    bullets: list[str] = None


@dataclass(frozen=True)
class Gallery:
    name: str
    items: list[Item]
