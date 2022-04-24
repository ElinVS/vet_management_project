# import pdb

from models.owner import Owner

import repositories.owner_repository as owner_repository

owner_repository.delete_all()

owner_1 = Owner("Alex", "Anderson", "alex@gmail.com", "0789 123 456", "1 The Street Edinburgh", "EH6 8HW", True)
# owner_2 = Owner("Benjamin")


owner_repository.save(owner_1)
# owner_repository.save(owner_2)

# 


# pdb.set_trace()