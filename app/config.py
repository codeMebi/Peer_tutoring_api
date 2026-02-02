import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:M%40rionette06@localhost:5432/peer_tutoring"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "super-secret-key")

