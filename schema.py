import typing
import strawberry
from crud import UserCrud
from validations import validation_email, validation_name, validation_phone


@strawberry.type
class User:
    id: strawberry.ID
    name: str
    email: str
    phone: str 
   

@strawberry.input
class UserInput:
    name: str
    email: str
    phone: str

@strawberry.type
class Query:
    @strawberry.field
    def select_user(self, id: strawberry.ID) -> User:
        user_crud = UserCrud()
        user = user_crud.select_user(id)
        return User(
            id=user["id"],
            name=user["name"],
            email=user["email"],
            phone=user["phone"]
        )
    

    @strawberry.field
    def select_total_users(self) -> typing.List[User]:
        user_crud = UserCrud()
        users = user_crud.select_total_users()
        
        user_instances = []
        for user in users:
                user_instance = User(
                    id=user["id"],
                    name=user["name"],
                    email=user["email"],
                    phone=user["phone"]
                )
                user_instances.append(user_instance)
            
        return user_instances
            
        
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, input: UserInput ) -> User:
        user = UserCrud()
        if  not validation_email(input.email):
            raise Exception("Ingresa un email valido.")
        
        if not validation_name(input.name):
            raise Exception("Ingresa un nombre valido.")
        
        
        if not validation_phone(input.phone):
            raise Exception("Ingresa un phone valido.")
        
        result = user.crear_user(name= input.name, email= input.email, phone= input.phone)
        user_response = User(id= result["id"], name= result["name"], phone=result["phone"], email=result["email"])
        return user_response
    

    @strawberry.mutation
    def update_user(self, id: strawberry.ID , input: UserInput) -> User:
        user = UserCrud()
        result = user.update_user(id= id, name= input.name, email= input.email, phone= input.phone)
        if result is None:
            return None
        
        user_response = User(id= result["id"], name= result["name"], email= result["email"], phone= result["phone"])
        return user_response
    

    @strawberry.mutation
    def delete_user(self, id: strawberry.ID) -> User:
        user = UserCrud()
        result = user.delete_user(id)
        if result is None:
            return None
        
        user_response = User(id= result["id"], name= result["name"], email= result["email"], phone= result["phone"])
        return user_response


schema = strawberry.Schema(query=Query, mutation=Mutation)
  