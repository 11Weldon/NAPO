class Auth:
    def __init__(self, db_handler):
      self.db_handler = db_handler

    def authenticate(self, user_id, password):
      session = self.db_handler.get_session()
      user = session.query(self.db_handler.models.User).filter_by(id=user_id).first()
      session.close()
      if user:

        return True
      return False

    def authorize(self, user, required_role):
      if user and user.role:
        if user.role.value == required_role:
          return True
      return False