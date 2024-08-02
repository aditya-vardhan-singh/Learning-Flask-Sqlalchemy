from sqlalchemy import Integer, String, ForeignKey, create_engine, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, relationship
from datetime import date
from dotenv import load_dotenv
import os

load_dotenv()

db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_database = os.getenv('DB_DATABASE')
database_url = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_database}'

engine = create_engine(database_url)


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__='students'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    date_of_birth: Mapped[Date] = mapped_column(Date, nullable=False)
    enrollment_date: Mapped[Date] = mapped_column(Date, nullable=False)


# Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)

# students = [
#     Student(name='Alice Smith', email='alice.smith@example.com', date_of_birth=date(2000, 5, 15), enrollment_date=date(2023, 8, 1)),
#     Student(name='Bob Johnson', email='bob.johnson@example.com', date_of_birth=date(1999, 10, 22), enrollment_date=date(2023, 8, 1)),
#     Student(name='Charlie Brown', email='charlie.brown@example.com', date_of_birth=date(2001, 2, 7), enrollment_date=date(2023, 8, 1)),
#     Student(name='David Lee', email='david.lee@example.com', date_of_birth=date(1998, 4, 12), enrollment_date=date(2023, 9, 1)),
#     Student(name='Emily Davis', email='emily.davis@example.com', date_of_birth=date(2002, 7, 25), enrollment_date=date(2023, 9, 1)),
#     Student(name='Frank Wilson', email='frank.wilson@example.com', date_of_birth=date(2000, 11, 30), enrollment_date=date(2023, 9, 1)),
#     Student(name='Grace Moore', email='grace.moore@example.com', date_of_birth=date(1997, 3, 16), enrollment_date=date(2023, 9, 1)),
#     Student(name='Henry Taylor', email='henry.taylor@example.com', date_of_birth=date(1999, 6, 22), enrollment_date=date(2023, 9, 1)),
#     Student(name='Ivy Martinez', email='ivy.martinez@example.com', date_of_birth=date(2001, 8, 9), enrollment_date=date(2023, 9, 1)),
#     Student(name='Jack Lewis', email='jack.lewis@example.com', date_of_birth=date(2002, 9, 14), enrollment_date=date(2023, 10, 1)),
#     Student(name='Kara Wilson', email='kara.wilson@example.com', date_of_birth=date(2000, 12, 30), enrollment_date=date(2023, 10, 1)),
#     Student(name='Liam Walker', email='liam.walker@example.com', date_of_birth=date(1998, 11, 15), enrollment_date=date(2023, 10, 1)),
#     Student(name='Mia Clark', email='mia.clark@example.com', date_of_birth=date(1999, 1, 18), enrollment_date=date(2023, 10, 1)),
#     Student(name='Paula Green', email='paula.green@example.com', date_of_birth=date(1997, 7, 31), enrollment_date=date(2023, 11, 1)),
#     Student(name='Quinn Scott', email='quinn.scott@example.com', date_of_birth=date(1998, 8, 14), enrollment_date=date(2023, 11, 1)),
#     Student(name='Ryan Allen', email='ryan.allen@example.com', date_of_birth=date(2000, 9, 19), enrollment_date=date(2023, 12, 1)),
#     Student(name='Sophie King', email='sophie.king@example.com', date_of_birth=date(1999, 10, 21), enrollment_date=date(2023, 12, 1)),
#     Student(name='Thomas Wright', email='thomas.wright@example.com', date_of_birth=date(1998, 11, 12), enrollment_date=date(2023, 12, 1)),
#     Student(name='Uma Lewis', email='uma.lewis@example.com', date_of_birth=date(2000, 12, 5), enrollment_date=date(2023, 12, 1)),
#     Student(name='Victor Carter', email='victor.carter@example.com', date_of_birth=date(2001, 1, 27), enrollment_date=date(2024, 1, 1)),
#     Student(name='Wendy Nelson', email='wendy.nelson@example.com', date_of_birth=date(1999, 2, 23), enrollment_date=date(2024, 1, 1)),
#     Student(name='Xander Morris', email='xander.morris@example.com', date_of_birth=date(2000, 3, 15), enrollment_date=date(2024, 1, 1)),
#     Student(name='Yara Mitchell', email='yara.mitchell@example.com', date_of_birth=date(2001, 4, 7), enrollment_date=date(2024, 1, 1)),
#     Student(name='Zachary Roberts', email='zachary.roberts@example.com', date_of_birth=date(1998, 5, 18), enrollment_date=date(2024, 2, 1)),
#     Student(name='Alice Johnson', email='alice.johnson@example.com', date_of_birth=date(2000, 6, 11), enrollment_date=date(2024, 2, 1)),
#     Student(name='Bob Brown', email='bob.brown@example.com', date_of_birth=date(1999, 7, 23), enrollment_date=date(2024, 2, 1)),
#     Student(name='Charlie Green', email='charlie.green@example.com', date_of_birth=date(2001, 8, 14), enrollment_date=date(2024, 2, 1)),
#     Student(name='David Black', email='david.black@example.com', date_of_birth=date(1998, 9, 30), enrollment_date=date(2024, 3, 1)),
#     Student(name='Emily White', email='emily.white@example.com', date_of_birth=date(2002, 10, 12), enrollment_date=date(2024, 3, 1)),
#     Student(name='Frank Harris', email='frank.harris@example.com', date_of_birth=date(2000, 11, 24), enrollment_date=date(2024, 3, 1)),
#     Student(name='Grace Martinez', email='grace.martinez@example.com', date_of_birth=date(1997, 12, 8), enrollment_date=date(2024, 3, 1)),
#     Student(name='Henry Thompson', email='henry.thompson@example.com', date_of_birth=date(1999, 1, 20), enrollment_date=date(2024, 4, 1)),
#     Student(name='Ivy Evans', email='ivy.evans@example.com', date_of_birth=date(2001, 2, 15), enrollment_date=date(2024, 4, 1)),
#     Student(name='Jack Clark', email='jack.clark@example.com', date_of_birth=date(2002, 3, 28), enrollment_date=date(2024, 4, 1)),
#     Student(name='Kara Lewis', email='kara.lewis@example.com', date_of_birth=date(2000, 4, 10), enrollment_date=date(2024, 4, 1)),
#     Student(name='Liam Hill', email='liam.hill@example.com', date_of_birth=date(1998, 5, 22), enrollment_date=date(2024, 5, 1)),
#     Student(name='Mia Allen', email='mia.allen@example.com', date_of_birth=date(2002, 6, 14), enrollment_date=date(2024, 5, 1)),
#     Student(name='Nina Adams', email='nina.adams@example.com', date_of_birth=date(1999, 7, 31), enrollment_date=date(2024, 5, 1)),
#     Student(name='Oliver Baker', email='oliver.baker@example.com', date_of_birth=date(2001, 8, 12), enrollment_date=date(2024, 6, 1)),
#     Student(name='Paula Wilson', email='paula.wilson@example.com', date_of_birth=date(1998, 9, 18), enrollment_date=date(2024, 6, 1)),
#     Student(name='Quinn Moore', email='quinn.moore@example.com', date_of_birth=date(2000, 10, 25), enrollment_date=date(2024, 6, 1)),
#     Student(name='Ryan Young', email='ryan.young@example.com', date_of_birth=date(1999, 11, 13), enrollment_date=date(2024, 7, 1)),
#     Student(name='Sophie Martinez', email='sophie.martinez@example.com', date_of_birth=date(2001, 12, 4), enrollment_date=date(2024, 7, 1)),
#     Student(name='Thomas King', email='thomas.king@example.com', date_of_birth=date(2000, 1, 21), enrollment_date=date(2024, 7, 1))
# ]

# with Session() as session:
#     session.add_all(students)
#     session.commit()
#     session.close()
