# import pdb

from models.owner import Owner

import repositories.owner_repository as owner_repository

owner_repository.delete_all()

owner_1 = Owner("Alex", "Anderson", "alex@gmail.com", "0789 123 456", "1 The Street Edinburgh", "EH6 8HW", True)
owner_2 = Owner("Benjamin", "Benson", "ben@gmail.com", "0777 333 444", "2 The Other Street Edinburgh", "EH6 8HW", False)


owner_repository.save(owner_1)
owner_repository.save(owner_2)





# test_owner_select = owner_repository.select(2)
# print(test_owner_select.__dict__)

# owner_repository.delete(2)







# pdb.set_trace()