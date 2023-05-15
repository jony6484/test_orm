from sqlalchemy import create_engine, Column, Integer, String, or_
from sqlalchemy.orm import sessionmaker, declarative_base

# required:
Base = declarative_base()

# The table
class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))



def main():
    # making the connection and session:
    engine = create_engine(r'sqlite:///test.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    # For first time table creation or migration
    # Base.metadata.create_all(engine)

    # creating new rows
    student1 = Student(name='Jony', age=39, grade='First')
    student2 = Student(name='Bony', age=24, grade='Second')
    student3 = Student(name='Dony', age=67, grade='Last')

    # Inserting into the table
    session.ass(student1)
    session.add_all([student2, student3])
    session.commit()

    # data retrival:    .filter, .first, 
    students = session.query(Student)
    print([(student.name, student.id) for student in session.query(Student).order_by(Student.id)])
    student = students = students.filter((Student.age >= 30) | (Student.age<=70)).first()

    # updating data:
    student = session.query(Student).filter(Student.id == 2).first()
    student.name = "Kevin"
    session.commit()

    # delete a record:
    student = session.query(Student).filter(Student.name == "Kevin").first()
    session.delete(student)
    session.commit()

    print('done')    




if __name__ == '__main__':

    main()