from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from models import Contact, Email, Phone
from sqlalchemy.orm import joinedload



engine = create_engine("sqlite:///mynotes.db")
Session = sessionmaker(bind=engine)
session = Session()


contact_1 = Contact(fullname="Donald Duck")
session.add(contact_1)
session.commit()

email_1 = Email(email="doda@gmail.com",contact_id=contact_1.id)
session.add(email_1)
session.commit()

phone_1 = Phone(phone="380670000000",contact_id=contact_1.id)
session.add(phone_1)
session.commit()


contact_2 = Contact(fullname="Robin Gud")
session.add(contact_2)
session.commit()

email_2 = Email(email="rg@gmail.com",contact_id=contact_2.id)
session.add(email_2)
session.commit()

phone_2 = Phone(phone="380671111111",contact_id=contact_2.id)
session.add(phone_2)
session.commit()


contact_3 = Contact(fullname="Ben Jon")
session.add(contact_3)
session.commit()

email_3 = Email(email="bj@gmail.com",contact_id=contact_3.id)
session.add(email_3)
session.commit()

phone_3 = Phone(phone="380672222222",contact_id=contact_3.id)
session.add(phone_3)
session.commit()


# SELECT c.fullname ,e.email ,p.phone
# FROM contacts c
# left join emails e on c.id =e.contact_id
# left join phones p on c.id =p.contact_id