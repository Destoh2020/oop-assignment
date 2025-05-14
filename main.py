# creating
class smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self._storage = storage

    def getDetails(self):
        return f"{self.brand} {self.model} with {self._storage}GB storage"

    def upgrade_storage(self, additional_storage):
        self._storage += additional_storage
        print(f"storage upgraded to {self._storage}GB")

class AndroidPhone(smartphone):
    def __init__(self, brand, model, storage, android_version):
        super().__init__(brand, model, storage)
        self._android_version = android_version

    def getDetails(self):
        return f"{super().getDetails()}, Android {self._android_version}"

class IOS(smartphone):
    def __init__(self, brand, model, storage, ios_version):
        super().__init__(brand, model, storage)
        self._ios_version = ios_version

    def getDetails(self):
        return f"{super().getDetails()}, IOS {self._ios_version}"


android = AndroidPhone("Samsung", "Galaxy S22", 128, "13")
iphone = IOS("Apple", "iphone 14", 256, "16.0")

print(android.getDetails())
print(iphone.getDetails())

android.upgrade_storage(64)