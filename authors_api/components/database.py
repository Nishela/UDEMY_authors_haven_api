from authors_api.settings import env

DATABASES = {"default": env.db("DATABASE_URL")}
