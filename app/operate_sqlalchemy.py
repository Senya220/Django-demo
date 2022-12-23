from base_sqlalchemy import Product
from base_sqlalchemy import db_session

# #insert
# user = Product(name='liuhe')
# db_session.add(user)
# db_session.commit()
# db_session.close()

#query
users = db_session.query(Product).filter_by(name='liuhe').one()
print(users.id,users.name)