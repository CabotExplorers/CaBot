import os
import datetime

from dotenv import load_dotenv
from peewee import *

load_dotenv()

db = SqliteDatabase(os.getenv("DB"))


class Base(Model):
    class Meta:
        database = db


class KeyValue(Base):
    key = TextField(unique=True)
    value = TextField(null=True)

    class Meta:
        table_name = "values"


class Member(Base):
    discordID = IntegerField(unique=True)
    name = TextField(null=True)
    points = IntegerField(default=0)


class Channel(Base):
    discordID = IntegerField(unique=True)
    name = TextField()


class Message(Base):
    timestamp = TimestampField(default=datetime.datetime.now().timestamp())
    member = ForeignKeyField(Member, backref="member")
    channel = ForeignKeyField(Channel, backref="channel")
    message = TextField(null=True)
    embed = TextField(null=True)


class Verifier(Base):
    discordID = IntegerField(unique=True)
    name = TextField()
    role = TextField()
    unit = TextField(null=True)
