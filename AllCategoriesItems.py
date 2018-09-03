from sqlalchemy.pool import StaticPool
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup_catalog import Category, Base, CategoryItem, User

engine = create_engine('sqlite:///catalogapp.db')
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
User1 = User(name="Bob Stan", email="tinnyTim@udacity.com",
             picture='https://cdn.pixabay.com/photo/2015/03/'
             '04/22/35/head-659651_960_720.png')
session.add(User1)
session.commit()

User2 = User(name="Caro L.", email="caro4learning@gmail.com",
             picture='https://cdn.pixabay.com/photo/2017/01/'
             '31/19/07/avatar-2026510_960_720.png')
session.add(User2)
session.commit()

# Items List for Soccer
categorie1 = Category(user_id=2, name="Soccer")

session.add(categorie1)
session.commit()


CategoryItem1 = CategoryItem(user_id=2, name="Soccer cleats",
                             description="football boots or soccer shoes are"
                             " worn when playing football outdoor",
                             genre="Footwear", categorie=categorie1)

session.add(CategoryItem1)
session.commit()

CategoryItem2 = CategoryItem(user_id=2, name="Indoor soccer shoes",
                             description="Indoor soccer shoes worn when"
                             " playing football", genre="Footwear",
                             categorie=categorie1)

session.add(CategoryItem2)
session.commit()

CategoryItem3 = CategoryItem(user_id=2, name="Jersey",
                             description="Jersey Shirt for football",
                             genre="Apparel", categorie=categorie1)

session.add(CategoryItem3)
session.commit()

CategoryItem4 = CategoryItem(user_id=2, name="Short",
                             description="Short worn when playing football",
                             genre="Apparel", categorie=categorie1)

session.add(CategoryItem4)
session.commit()

CategoryItem5 = CategoryItem(user_id=2, name="Socks",
                             description="Socks worn when playing football",
                             genre="Apparel", categorie=categorie1)

session.add(CategoryItem5)
session.commit()

CategoryItem6 = CategoryItem(user_id=2, name="Soccer ball",
                             description="Soccer ball", genre="Equipment",
                             categorie=categorie1)

session.add(CategoryItem6)
session.commit()

CategoryItem7 = CategoryItem(user_id=2, name="Goalkeeper gloves",
                             description="Gloves worn by the Goalkeeper "
                             "during fottball match", genre="Apparel",
                             categorie=categorie1)

session.add(CategoryItem7)
session.commit()

CategoryItem8 = CategoryItem(user_id=2, name="Shin guards",
                             description="Shin protection worn during "
                             "fottball match", genre="Accessories",
                             categorie=categorie1)

session.add(CategoryItem8)
session.commit()

CategoryItem9 = CategoryItem(user_id=2, name="Ball bag",
                             description="Bag used to store soccer balls",
                             genre="Equipment", categorie=categorie1)

session.add(CategoryItem9)
session.commit()

CategoryItem10 = CategoryItem(user_id=2, name="Team Backpack",
                              description="Team Backpack", genre="Equipment",
                              categorie=categorie1)

session.add(CategoryItem10)
session.commit()

CategoryItem11 = CategoryItem(user_id=2, name="Sweatband",
                              description="Sweatband", genre="Accessories",
                              categorie=categorie1)

session.add(CategoryItem11)
session.commit()

CategoryItem12 = CategoryItem(user_id=2, name="Wristband",
                              description="Wristband", genre="Accessories",
                              categorie=categorie1)

session.add(CategoryItem12)
session.commit()


# Items list for Basketball
categorie2 = Category(user_id=2, name="Basketball")

session.add(categorie2)
session.commit()


CategoryItem13 = CategoryItem(user_id=2, name="Basketball shoes",
                              description="Lockdown basketball shoes",
                              genre="Footwear", categorie=categorie2)

session.add(CategoryItem13)
session.commit()

CategoryItem14 = CategoryItem(user_id=2, name="Basketball Jersey",
                              description="Basketball Jersey",
                              genre="Apparel", categorie=categorie2)

session.add(CategoryItem14)
session.commit()

CategoryItem15 = CategoryItem(user_id=2, name="Basketball short",
                              description="Basketball short", genre="Apparel",
                              categorie=categorie2)

session.add(CategoryItem15)
session.commit()

CategoryItem16 = CategoryItem(user_id=2, name="Basketball warm-up pants",
                              description="Basketball warm-up pants",
                              genre="Apparel", categorie=categorie2)

session.add(CategoryItem16)
session.commit()

CategoryItem17 = CategoryItem(user_id=2, name="Game Basketball",
                              description="Ball used to play basketball",
                              genre="Equipment", categorie=categorie2)

session.add(CategoryItem17)
session.commit()

CategoryItem18 = CategoryItem(user_id=2, name="Basketball net",
                              description="Basketball net", genre="Equipment",
                              categorie=categorie2)

session.add(CategoryItem18)
session.commit()

CategoryItem19 = CategoryItem(user_id=2, name="Sweatband",
                              description="Basketball Sweatband",
                              genre="Accessories", categorie=categorie2)

session.add(CategoryItem19)
session.commit()

CategoryItem20 = CategoryItem(user_id=2, name="Protective pads or sleeve",
                              description="Basketball knee, elbow, "
                              "shin sleeve", genre="Accessories",
                              categorie=categorie2)

session.add(CategoryItem20)
session.commit()

CategoryItem21 = CategoryItem(user_id=2, name="Socks",
                              description="Basketball socks", genre="Apparel",
                              categorie=categorie2)

session.add(CategoryItem21)
session.commit()


# Items list for Snowboarding
categorie3 = Category(user_id=1, name="Snowboarding")

session.add(categorie3)
session.commit()


CategoryItem22 = CategoryItem(user_id=1, name="Goggles",
                              description="The wearing of ultra-violet"
                              "-absorbing goggles is recommended even on "
                              "hazy or cloudy days as ultra-violet light "
                              "can penetrate clouds", genre="Apparel",
                              categorie=categorie3)

session.add(CategoryItem22)
session.commit()

CategoryItem23 = CategoryItem(user_id=1, name="Snowboard",
                              description="Snowboard", genre="Equipment",
                              categorie=categorie3)

session.add(CategoryItem23)
session.commit()

CategoryItem24 = CategoryItem(user_id=1, name="Mittens and Gloves",
                              description="Snowboarding Mittens and Gloves",
                              genre="Apparel", categorie=categorie3)

session.add(CategoryItem24)
session.commit()

CategoryItem25 = CategoryItem(user_id=1, name="Scarves and Neck warmers",
                              description="Snowboarding neck warmers and "
                              "Scarves", genre="Accessories",
                              categorie=categorie3)

session.add(CategoryItem25)
session.commit()

CategoryItem26 = CategoryItem(user_id=1, name="Pants",
                              description="Snowboarding insulated Pants",
                              genre="Apparel", categorie=categorie3)

session.add(CategoryItem26)
session.commit()

CategoryItem27 = CategoryItem(user_id=1, name="Jackets",
                              description="Snowboarding insulated Jackets",
                              genre="Apparel", categorie=categorie3)

session.add(CategoryItem27)
session.commit()

CategoryItem28 = CategoryItem(user_id=1, name="Toque", description="Toque",
                              genre="Apparel", categorie=categorie3)

session.add(CategoryItem28)
session.commit()

CategoryItem30 = CategoryItem(user_id=1, name="Helmet",
                              description="Snowboard Helmet", genre="Apparel",
                              categorie=categorie3)

session.add(CategoryItem30)
session.commit()

CategoryItem31 = CategoryItem(user_id=1, name="Boots",
                              description="Snowboard boots", genre="Footwear",
                              categorie=categorie3)

session.add(CategoryItem31)
session.commit()

CategoryItem32 = CategoryItem(user_id=1, name="Bindings",
                              description="Snowboard bindings",
                              genre="Footwear", categorie=categorie3)

session.add(CategoryItem32)
session.commit()

CategoryItem33 = CategoryItem(user_id=1, name="Snowboard Bag",
                              description="Snowboard bags",
                              genre="Accessories", categorie=categorie3)

session.add(CategoryItem33)
session.commit()

CategoryItem34 = CategoryItem(user_id=1, name="Snowboard Wrist",
                              description="Snowboard Wrist",
                              genre="Accessories", categorie=categorie3)

session.add(CategoryItem34)
session.commit()


print "added categories items!"
