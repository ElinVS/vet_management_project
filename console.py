# import pdb

from models.owner import Owner

import repositories.owner_repository as owner_repository


owner_1 = Owner("Alex")
owner_repository.save(owner_1)




# pdb.set_trace()