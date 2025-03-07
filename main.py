from fastapi import FastAPI, Depends, HTTPException, status, Query, UploadFile, File
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from datetime import datetime, timedelta
from schemas import *
from database import *
from models import *
import os
from auth import SECRET_KEY, ALGORITHM
from auth import (
    get_password_hash,
    verify_password,
    create_access_token,
    SECRET_KEY,
    ALGORITHM,
)


app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

UPLOAD_DIRECTORY = "uploads/"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)


@app.get("/")
def home():
    return {"message": "FastAPI is running!"}

# Register a new user
@app.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Login and get JWT token
@app.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == form_data.username).first()
    if not db_user or not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}

# Protected route
@app.get("/me", response_model=UserResponse)
def read_users_me(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    db_user = db.query(User).filter(User.email == email).first()
    if db_user is None:
        raise credentials_exception
    return db_user
  
  

# Dependency to get the current user from the token
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception
    return user

# Create a new post
@app.post("/posts", response_model=PostResponse)
def create_post(post: PostCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_post = Post(
        main_content=post.main_content,
        image=post.image,
        user_id=current_user.id,
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
  
# Upvote a post
@app.post("/posts/{post_id}/upvote")
def upvote_post(post_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    db_post.upvotes += 1
    db.commit()
    db.refresh(db_post)
    return {"message": "Post upvoted successfully"}

# Downvote a post
@app.post("/posts/{post_id}/downvote")
def downvote_post(post_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    db_post.downvotes += 1
    db.commit()
    db.refresh(db_post)
    return {"message": "Post downvoted successfully"}


# Create a Collaboration Post
@app.post("/collabs", status_code=status.HTTP_201_CREATED)
def create_collab_post(
    collab_post: CollabPostCreate, 
    current_user: User = Depends(get_current_user), 
    db: Session = Depends(get_db)
):
    db_collab = CollabPost(
        project_name=collab_post.project_name,
        description=collab_post.description,
        skills_required=",".join(collab_post.skills_required),
        user_id=current_user.id,
    )
    db.add(db_collab)
    db.commit()
    db.refresh(db_collab)
    return {"data": db_collab}

# Apply to a Collaboration Post
@app.post("/collabs/{collab_id}/apply", status_code=status.HTTP_200_OK)
def apply_to_collab(
    collab_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_collab = db.query(CollabPost).filter(CollabPost.id == collab_id).first()
    if not db_collab:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Collaboration post not found")

    application = CollabApplication(
        collab_post_id=collab_id,
        user_id=current_user.id
    )
    db.add(application)
    db.commit()
    return {"data": {"message": "Applied successfully"}}

# Get details of a single Collaboration Post
@app.get("/collabs/{collab_id}", status_code=status.HTTP_200_OK)
def get_collab_post(
    collab_id: int, 
    db: Session = Depends(get_db)
):
    db_collab = db.query(CollabPost).filter(CollabPost.id == collab_id).first()
    if not db_collab:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Collaboration post not found")
    return {"data": db_collab}

# List all Collaboration Posts with Pagination
@app.get("/collabs", status_code=status.HTTP_200_OK)
def list_collab_posts(
    db: Session = Depends(get_db),
    skip: int = Query(0, alias="offset"),
    limit: int = Query(10, alias="limit")
):
    collab_posts = db.query(CollabPost).offset(skip).limit(limit).all()
    return {"data": collab_posts}

# Create User Profile
@app.post("/users/profile", status_code=status.HTTP_201_CREATED)
def create_user_profile(
    profile: UserProfileCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_profile = UserProfile(
        name=profile.name,
        bio=profile.bio,
        skills=",".join(profile.skills),
        user_id=current_user.id
    )
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return {"data": db_profile}

# Upload Profile Picture
@app.post("/users/profile/picture", status_code=status.HTTP_200_OK)
def upload_profile_picture(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    file_path = f"{UPLOAD_DIRECTORY}{current_user.id}_{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    if not current_user.profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found")
    
    current_user.profile.profile_picture = file_path
    db.commit()
    return {"data": {"profile_picture": file_path}}

# Get User Profile
@app.get("/users/profile", status_code=status.HTTP_200_OK)
def get_user_profile(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    profile = db.query(UserProfile).filter(UserProfile.user_id == current_user.id).first()
    if not profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found")
    return {"data": profile}

# Edit User Profile
@app.put("/users/profile", status_code=status.HTTP_200_OK)
def edit_user_profile(
    profile_update: UserProfileUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    profile = db.query(UserProfile).filter(UserProfile.user_id == current_user.id).first()
    if not profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found")
    
    if profile_update.name:
        profile.name = profile_update.name
    if profile_update.bio:
        profile.bio = profile_update.bio
    if profile_update.skills:
        profile.skills = ",".join(profile_update.skills)
    
    db.commit()
    return {"data": profile}
