from datetime import datetime
from core.models import Notification
from core.db import get_session


class NotificationManager:
    def __init__(self):
        pass

    def create_notification(self, user_id, message):
        """Creates a new notification for a user."""
        session = get_session()
        try:
            new_notification = Notification(user_id=user_id, message=message, date=datetime.now())
            session.add(new_notification)
            session.commit()
            return new_notification
        except Exception as e:
            session.rollback()
            print(f"Error creating notification: {e}")
            return None
        finally:
            session.close()

    def get_user_notifications(self, user_id):
        """Retrieves all notifications for a user."""
        session = get_session()
        try:
            notifications = session.query(Notification).filter_by(user_id=user_id).all()
            return notifications
        except Exception as e:
            print(f"Error getting user notifications: {e}")
            return []
        finally:
            session.close()

    def get_all_notifications(self):
        """Retrieves all notifications from the database."""
        session = get_session()
        try:
            all_notifications = session.query(Notification).all()
            return all_notifications
        except Exception as e:
            print(f"Error getting all notifications: {e}")
            return []
        finally:
            session.close()

    def delete_notification(self, notification_id):
        session = get_session()
        try:
            notification = session.query(Notification).get(notification_id)
            if notification:
                session.delete(notification)
                session.commit()
            else:
                print("Notification not found")
        except Exception as e:
            print(f"Error delete notification: {e}")
        finally:
            session.close()
