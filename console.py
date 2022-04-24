# import pdb

from models.owner import Owner
from models.pet import Pet

import repositories.owner_repository as owner_repository
import repositories.pet_repository as pet_repository

owner_repository.delete_all()

owner_1 = Owner("Alex", "Anderson", "alex@gmail.com", "0789 123 456", "1 The Street Edinburgh", "EH6 8HW", True)
owner_2 = Owner("Benjamin", "Benson", "ben@gmail.com", "0777 333 444", "2 The Other Street Edinburgh", "EH6 8HW", False)


owner_repository.save(owner_1)
owner_repository.save(owner_2)

pet_1 = Pet("Marvin", "Dog", "01-02-2017", owner_1, "Re-curring stomach issues. Last working treatment was on 03-03-2022")

pet_repository.save(pet_1)





# test_owner_select = owner_repository.select(2)
# print(test_owner_select.__dict__)

# owner_repository.delete(2)







# pdb.set_trace()