from Object import Object


class Bag:
    def __init__(self, max_object: int, collection: list[Object]):
        if collection is None:
            collection = []

        self.max_object = max_object
        self.collection = collection
        self.counter = len(collection)

    def PickUpObject(self, obj: Object):
        if self.counter < self.max_object:
            self.collection.append(obj)

    def DropObject(self, obj: Object):
        if obj in self.collection:
            self.collection.remove(obj)

    def get_collection(self):
        return self.collection
