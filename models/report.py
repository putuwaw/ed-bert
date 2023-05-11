from sqlalchemy import Column, String, Integer, MetaData, Table

metadata = MetaData()

report = Table('report', metadata,
               Column('id', Integer, primary_key=True,
                      autoincrement=True),
               Column('text', String(500)),
               Column('predicted', String(45)),
               Column('actual', String(45))
               )
