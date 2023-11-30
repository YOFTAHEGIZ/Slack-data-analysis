# create_tables.py
from sqlalchemy import ForeignKey, MetaData, Table, Column, Integer, String, Float
from postgrlsql_connection import create_database_engine

def create_tables(engine):
    metadata = MetaData()
    engine = create_database_engine()

    message_table = Table(
        'message_table',
        metadata,
        Column('id', Integer, primary_key=True),
        Column('msg_type', String),  
        Column('msg_content', String),
        Column('sender_name', String),
        Column('msg_sent_time', Float),  
        Column('msg_dist_type', String),
        Column('time_thread_start', Float),  
        Column('reply_count', Integer),
        Column('reply_users_count', Integer)
        )
    
    user_table = Table(
        'user_table',
        metadata,
        Column('id', Integer, primary_key=True),
        Column('user_id', Integer, unique=True),  
        Column('user_name', String),
    )

    reaction_table = Table(
        'reaction_table',
        metadata,
        Column('id', Integer, primary_key=True),
        Column('reaction_name', String),
        Column('reaction_count', Integer),
        Column('reaction_users_count', Integer),
        Column('message', String),
        Column('user_id', Integer, ForeignKey('user_table.user_id')),  
        Column('channel', String),
    )


    metadata.create_all(engine)

    print('Tables are created succesfully')