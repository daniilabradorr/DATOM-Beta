# your_app/utils.py

from .models import UserActivityLog

def log_user_action(user, action, additional_data=None):
    UserActivityLog.objects.create(user=user, action=action, additional_data=additional_data)
