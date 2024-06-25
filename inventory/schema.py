import graphene

from graphene_django import DjangoObjectType, DjangoListField 
from .models import LibraryItem 


class LibraryItemType(DjangoObjectType): 
    class Meta:
        model = LibraryItem
        fields = "__all__"


class Query(graphene.ObjectType):
    all_items = graphene.List(LibraryItemType)
    item = graphene.Field(LibraryItemType, item_id=graphene.Int())

    def resolve_all_items(self, info, **kwargs):
        return LibraryItem.objects.all()

    def resolve_item(self, info, item_id):
        return LibraryItem.objects.get(pk=item_id)


class LibraryItemInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    author = graphene.String()
    year_published = graphene.String()
    rating = graphene.Int()



class CreateLibraryItem(graphene.Mutation):
    class Arguments:
        item_data = LibraryItemInput(required=True)

    item = graphene.Field(LibraryItemType)

    @staticmethod
    def mutate(root, info, item_data=None):
        item_instance = LibraryItem( 
            title=item_data.title,
            author=item_data.author,
            year_published=item_data.year_published,
            rating=item_data.rating
        )
        item_instance.save()
        return CreateLibraryItem(item=item_instance)


class UpdateLibraryItem(graphene.Mutation):
    class Arguments:
        item_data = LibraryItemInput(required=True)

    item = graphene.Field(LibraryItemType)

    @staticmethod
    def mutate(root, info, item_data=None):
        item_instance = LibraryItem.objects.get(pk=item_data.id)

        if item_instance:
            item_instance.title = item_data.title
            item_instance.author = item_data.author
            item_instance.year_published = item_data.year_published
            item_instance.rating = item_data.rating
            item_instance.save()

            return UpdateLibraryItem(item=item_instance)
        return UpdateLibraryItem(item=None)



class DeleteLibraryItem(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    item = graphene.Field(LibraryItemType)

    @staticmethod
    def mutate(root, info, id):
        item_instance = LibraryItem.objects.get(pk=id)
        item_instance.delete()

        return True




class Mutation(graphene.ObjectType):
    create_item = CreateLibraryItem.Field()
    update_item = UpdateLibraryItem.Field()
    delete_item = DeleteLibraryItem.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
