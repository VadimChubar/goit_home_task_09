from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from models import Contact, Email, Phone
import argparse
from sqlalchemy import update


parser = argparse.ArgumentParser(description='Phone Book')
parser.add_argument("--action", "-a", help="Command: insert, update_phone, update_email, update_contact, "
                                           "show_all, show_contact, remove", required=True)
parser.add_argument("--fullname")
parser.add_argument("--phone")
parser.add_argument("--email")
parser.add_argument("--id")

args = vars(parser.parse_args())

action = args.get("action")
fullname = args.get("fullname")
phone = args.get("phone")
email = args.get("email")
contact_id = args.get("id")


def main():

    engine = create_engine("sqlite:///mynotes.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    match action:

        case "insert":

            contact_ = Contact(fullname=fullname)
            session.add(contact_)
            session.commit()

            email_ = Email(email=email, contact_id=contact_.id)
            session.add(email_)
            session.commit()

            phone_ = Phone(phone=phone, contact_id=contact_.id)
            session.add(phone_)
            session.commit()

            print("Contact inserted")

        case 'update_contact':
            fn = session.query(Contact).filter(Contact.id == contact_id).first()
            if fn:
                session.execute(update(Contact).where(Contact.id == contact_id).values(fullname=fullname))
            print("Contact updated")
            session.commit()

        case 'update_phone':
            ph = session.query(Phone).filter(Phone.contact_id == contact_id).first()
            if ph:
                session.execute(update(Phone).where(Phone.contact_id == contact_id).values(phone=phone))
            print("Phone updated")
            session.commit()

        case 'update_email':
            em = session.query(Email).filter(Email.contact_id == contact_id).first()
            if em:
                session.execute(update(Email).where(Email.contact_id == contact_id).values(email=email))
            print("Email updated")
            session.commit()

        case "show_contact":
            result = session.query(Contact.id, Contact.fullname, Phone.phone).select_from(Contact).join(Phone)\
                .filter(Contact.fullname == fullname)
            for i in result:
                print(i)

        case "show_all":
            result = session.query(Contact.id, Contact.fullname, Phone.phone).select_from(Contact).join(Phone).all()
            for i in result:
                print(i)

        case "remove":
            con = session.query(Contact).filter(Contact.id == contact_id).first()
            session.delete(con)
            print("Contact deleted")
            session.commit()

        case _:
            print("Unknown command!")

    session.close()


if __name__ == '__main__':
    main()








