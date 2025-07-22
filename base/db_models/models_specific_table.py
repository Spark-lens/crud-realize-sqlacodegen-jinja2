from typing import List

from sqlalchemy import Column, ForeignKeyConstraint, Integer, PrimaryKeyConstraint, String, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class Parts(Base):
    __tablename__ = 'parts'
    __table_args__ = (
        PrimaryKeyConstraint('part_id', name='parts_pkey'),
    )

    part_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    part_name: Mapped[str] = mapped_column(String(255))

    vendor: Mapped[List['Vendors']] = relationship('Vendors', secondary='vendor_parts', back_populates='part')


class Vendors(Base):
    __tablename__ = 'vendors'
    __table_args__ = (
        PrimaryKeyConstraint('vendor_id', name='vendors_pkey'),
    )

    vendor_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    vendor_name: Mapped[str] = mapped_column(String(255))

    part: Mapped[List['Parts']] = relationship('Parts', secondary='vendor_parts', back_populates='vendor')


t_vendor_parts = Table(
    'vendor_parts', Base.metadata,
    Column('vendor_id', Integer, primary_key=True, nullable=False),
    Column('part_id', Integer, primary_key=True, nullable=False),
    ForeignKeyConstraint(['part_id'], ['parts.part_id'], ondelete='CASCADE', onupdate='CASCADE', name='vendor_parts_part_id_fkey'),
    ForeignKeyConstraint(['vendor_id'], ['vendors.vendor_id'], ondelete='CASCADE', onupdate='CASCADE', name='vendor_parts_vendor_id_fkey'),
    PrimaryKeyConstraint('vendor_id', 'part_id', name='vendor_parts_pkey')
)
