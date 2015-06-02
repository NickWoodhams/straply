
from app.helpers import id_generator

print("SECRET_KEY = '%s'\n") % id_generator(24)
print("SECURITY_PASSWORD_SALT = '%s'") % id_generator(24)
print("SECURITY_REMEMBER_SALT = '%s'") % id_generator(24)
print("SECURITY_RESET_SALT = '%s'") % id_generator(24)
