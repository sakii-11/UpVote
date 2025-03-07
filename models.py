from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    main_content = Column(Text, nullable=False)
    image = Column(String, nullable=True)  # Optional image URL
    upvotes = Column(Integer, default=0)
    downvotes = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey("users.id"))

    # Relationship to User
    user = relationship("User", back_populates="posts")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    profile = relationship("UserProfile", uselist=False, back_populates="user")
    posts = relationship("Post", back_populates="user")
    
class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    bio = Column(Text, nullable=True)
    skills = Column(String, nullable=True)
    profile_picture = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    user = relationship("User", back_populates="profile")
    
    

class CollabPost(Base):
    __tablename__ = "collab_posts"

    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    skills_required = Column(String, nullable=False)  # Stored as comma-separated values
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="collab_posts")