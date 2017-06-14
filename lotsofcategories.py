from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Sportista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# ---------------
# Soccer category
# ---------------
category1 = Category(user_id=1, name="Soccer")

session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Two shinguards", description="Guards for your shins. (x2)",
              category=category1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Shinguards", description="Guards for your shins.",
              category=category1)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Soccer Cleats", description="Soccer boot studs.",
              category=category1)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Jersey", description="Manchester United jersey.",
              category=category1)

session.add(item4)
session.commit()

# ---------------
# Basketball category
# ---------------
category2 = Category(user_id=1, name="Basketball")

session.add(category2)
session.commit()

# ---------------
# Baseball category
# ---------------
category3 = Category(user_id=1, name="Baseball")

session.add(category3)
session.commit()

item1 = Item(user_id=1, name="Bat", description="Wooden club for hitting baseballs.",
              category=category3)

session.add(item1)
session.commit()

# ---------------
# Frisbee category
# ---------------
category4 = Category(user_id=1, name="Frisbee")

session.add(category4)
session.commit()

item1 = Item(user_id=1, name="Frisbee", description="Round disc for throwing and catching.",
              category=category4)

session.add(item1)
session.commit()

# ---------------
# Snowboarding category
# ---------------
category5 = Category(user_id=1, name="Snowboarding")

session.add(category5)
session.commit()

item1 = Item(user_id=1, name="Goggles", description="To protect your eyes.",
              category=category5)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Snowboard", description="A board to ride the snow on.",
              category=category5)

session.add(item2)
session.commit()

# ---------------
# Rock Climbing category
# ---------------
category6 = Category(user_id=1, name="Rock Climbing")

session.add(category6)
session.commit()

# ---------------
# Foosball category
# ---------------
category7 = Category(user_id=1, name="Foosball")

session.add(category7)
session.commit()

# ---------------
# Skating category
# ---------------
category8 = Category(user_id=1, name="Skating")

session.add(category8)
session.commit()

item1 = Item(user_id=1, name="Pair of skates", description="For skating on ice..",
              category=category8)

session.add(item1)
session.commit()

# ---------------
# Hockey category
# ---------------
category9 = Category(user_id=1, name="Hockey")

session.add(category9)
session.commit()

item1 = Item(user_id=1, name="Stick", description="Hockey stick.",
              category=category9)

session.add(item1)
session.commit()


print "added menu items!"