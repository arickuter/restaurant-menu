import sys
from sqlalchemy imoprt
Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import
declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()


######## Insert at end of file ########

engine = create_engine(
'sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)
