from .apps import UsersConfig
from .routers import router

app_name = UsersConfig.name

urlpatterns = (
    *router.urls,
)
