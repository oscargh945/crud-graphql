import typing
import strawberry
from enum import Enum

users = []

@strawberry.type
class User:
    id: strawberry.ID
    name: str
    email: str
    phone: int


@strawberry.input
class UserInput:
    name: str
    email: str
    phone: int


@strawberry.type
class Query:
    @strawberry.field
    def get_user(self, ) -> typing.List[User]:
        return users 


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_user(self, input: typing.List[UserInput]) -> typing.List[User]:
        for item in input:
            print(f"agregando un usuraio con el nombre {item.name}, el email {item.email} y el telefono {item.phone}")
            user = User(id=1, name=item.name, email=item.email, phone=item.phone)
            count = len(users)
            if count != 0:
                user.id = count + 1

            users.append(user)
        
        return users

        
schema = strawberry.Schema(mutation=Mutation, query=Query)
