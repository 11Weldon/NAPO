from core.db import create_database, get_session
from ui.cli import main_menu
from core.logic import create_user
from core.roles import Role
from core.models import User

if __name__ == "__main__":
    create_database()
    session = get_session()
    # Проверяем, существует ли админ
    admin = session.query(User).filter(User.name == 'admin').first()
    if not admin:
      # Создаем администратора (если его еще нет)
      admin_data = {'name': 'admin', 'role': 'admin'}
      admin = create_user(admin_data)
      if admin:
          try:
            # Получаем ID админа
            admin_id = session.query(User).filter(User.name == 'admin').first().id
            print(f"Admin user created with ID: {admin_id}")
          except Exception as e:
            print(f"Error: Can't get admin ID: {e}")
      else:
         print("Error create admin")
    else:
        print(f"Admin user with ID: {admin.id} already exist.")
    session.close()
    main_menu()