
from user.models import Users

class Common():
    def fetch_user_details(self, user_id):
        return Users.objects.get(id=user_id) 