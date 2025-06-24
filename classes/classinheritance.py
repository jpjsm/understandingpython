from typing import Iterable


class Me:
    """sample class friend."""

    def __init__(self, me: str) -> None:
        self.me = str(me)
        self.parents = (None, None)
        self.siblings = set()
        self.spouse = None
        self.children = set()

    def parents_update(self, father: str, mother: str):
        self.parents = (father, mother)

    def siblings_add(self, siblings: Iterable[str]):
        self.siblings.update(siblings)

    def spouse_update(self, spouse: str):
        self.spouse = spouse

    def children_add(self, children: Iterable[str]):
        self.children.update(children)


class My_Friends(Me):
    """my and my friends."""

    def __init__(self, me: str) -> None:
        super().__init__(me)
        self.friends = set()

    def friends_add(self, friends: Iterable[str]):
        self.friends.update(friends)


jp = Me("jp")
print(f"{jp.me=}")

maridita = My_Friends("maridita")
print(f"{maridita.me=}")
