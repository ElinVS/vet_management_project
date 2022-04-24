# import pdb

from models.owner import Owner
from models.pet import Pet

import repositories.owner_repository as owner_repository
import repositories.pet_repository as pet_repository

owner_repository.delete_all()
pet_repository.delete_all()

owner_1 = Owner("Alex", "Anderson", "alex@gmail.com", "0789 123 456", "1 The Street Edinburgh", "EH6 8HW", True)
owner_2 = Owner("Benjamin", "Benson", "ben@gmail.com", "0777 333 444", "2 The Other Street Edinburgh", "EH6 8HW", False)


owner_repository.save(owner_1)
owner_repository.save(owner_2)

pet_1 = Pet("Marvin", "Dog", "01-02-2017", owner_1, "Re-curring stomach issues. Last working treatment was on 03-03-2022")
pet_2 = Pet("Milo", "Cat", "02-02-2012", owner_2, "Persistant skin infection on left paw. Last treatment given 02-03-2022")

pet_repository.save(pet_1)
pet_repository.save(pet_2)

# test_owner_selectall = owner_repository.select_all()
# print(test_owner_selectall[1].__dict__)

# test_owner_select = owner_repository.select(2)
# print(test_owner_select.__dict__)

# owner_repository.delete(2)


# test_pet_selectall = pet_repository.select_all()
# print(test_pet_selectall[0].__dict__)

# test_pet_select = pet_repository.select(1)
# print(test_pet_select.__dict__)

# pet_repository.delete(2)

pet_1.owner.id = 2
pet_repository.update(pet_1)


# pdb.set_trace()