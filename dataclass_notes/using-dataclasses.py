import inspect
from dataclasses import dataclass, astuple, asdict, field
from pprint import pprint


# frozen=True makes the class immutable
@dataclass(frozen=True, order=True)
class Comment:
    id: int = field()   # default value
    text: str = ""      # default value
    text_2: str = field(default="")  # also a valid default value
    replies: list[int] = field(default_factory=list)   # default factory
    replies_2: list[int] = field(default_factory=list, compare=False, hash=False, repr=False)
    # default factory, but not compared, hashed, or represented


def main():
    comment = Comment(1, 'hello')
    print(comment)
    # build-in functions
    print(astuple(comment))
    print(asdict(comment))
    # inspect module
    pprint(inspect.getmembers(Comment, inspect.isfunction))

    comment_2 = Comment(2, '')
    print(comment_2)
    print(astuple(comment_2))
    print(asdict(comment_2))
    pprint(inspect.getmembers(Comment, inspect.isfunction))


if __name__ == '__main__':
    main()
