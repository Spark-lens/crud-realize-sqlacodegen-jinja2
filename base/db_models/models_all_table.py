from typing import List, Optional

from sqlalchemy import BigInteger, Column, Date, ForeignKeyConstraint, Integer, LargeBinary, PrimaryKeyConstraint, String, Table
from db_models.base import Base, Mapped, mapped_column, relationship
import datetime


class MockData(Base):
    __tablename__ = 'mock_data'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='mock_data_pkey'),
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    make: Mapped[str] = mapped_column(String(100))
    model: Mapped[str] = mapped_column(String(100))
    price: Mapped[Optional[str]] = mapped_column(String(20))


class Parts(Base):
    __tablename__ = 'parts'
    __table_args__ = (
        PrimaryKeyConstraint('part_id', name='parts_pkey'),
    )

    part_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    part_name: Mapped[str] = mapped_column(String(255))

    vendor: Mapped[List['Vendors']] = relationship('Vendors', secondary='vendor_parts', back_populates='part')


class Person(Base):
    __tablename__ = 'person'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='person_pkey'),
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    gender: Mapped[str] = mapped_column(String(15))
    date_of_birth: Mapped[datetime.date] = mapped_column(Date)
    email: Mapped[Optional[str]] = mapped_column(String(150))
    country_of_birth: Mapped[Optional[str]] = mapped_column(String(50))


class PidTable(Base):
    __tablename__ = 'pid_table'
    __table_args__ = (
        PrimaryKeyConstraint('pid', name='pid_table_pkey'),
    )

    pid: Mapped[int] = mapped_column(Integer, primary_key=True)


class Vendors(Base):
    __tablename__ = 'vendors'
    __table_args__ = (
        PrimaryKeyConstraint('vendor_id', name='vendors_pkey'),
    )

    vendor_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    vendor_name: Mapped[str] = mapped_column(String(255))

    part: Mapped[List['Parts']] = relationship('Parts', secondary='vendor_parts', back_populates='vendor')


class PartDrawings(Parts):
    __tablename__ = 'part_drawings'
    __table_args__ = (
        ForeignKeyConstraint(['part_id'], ['parts.part_id'], ondelete='CASCADE', onupdate='CASCADE', name='part_drawings_part_id_fkey'),
        PrimaryKeyConstraint('part_id', name='part_drawings_pkey')
    )

    part_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    file_extension: Mapped[str] = mapped_column(String(5))
    drawing_data: Mapped[bytes] = mapped_column(LargeBinary)


t_vendor_parts = Table(
    'vendor_parts', Base.metadata,
    Column('vendor_id', Integer, primary_key=True, nullable=False),
    Column('part_id', Integer, primary_key=True, nullable=False),
    ForeignKeyConstraint(['part_id'], ['parts.part_id'], ondelete='CASCADE', onupdate='CASCADE', name='vendor_parts_part_id_fkey'),
    ForeignKeyConstraint(['vendor_id'], ['vendors.vendor_id'], ondelete='CASCADE', onupdate='CASCADE', name='vendor_parts_vendor_id_fkey'),
    PrimaryKeyConstraint('vendor_id', 'part_id', name='vendor_parts_pkey')
)
