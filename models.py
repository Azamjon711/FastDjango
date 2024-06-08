from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType
from database import Base


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    product = relationship('Product', back_populates='category')

class Product(Base):

    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(Text)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', back_populates='product')
    order = relationship('Order', back_populates='product')


class Order(Base):

    __tablename__ = 'order'

    OrderChoices = (
        ("PENDING", "pending"),
        ("TRANSIT", 'transit'),
        ("DELIVERED", "delivered")
    )

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    count = Column(Integer)
    order_status = Column(ChoiceType(choices=OrderChoices), default="PENDING")
    users = relationship('User', back_populates='orders')
    product = relationship('Product', back_populates='order')
