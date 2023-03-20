from .models import Usuario
from django.contrib.auth.hashers import check_password


def VerifyPwd(request):
  try:
    user_pwd = Usuario.objects.filter(codigo=request.POST['username'])
    pwd_checked = check_password(request.POST['password'],user_pwd[0].contrasena)
    if  pwd_checked:
      return user_pwd
    else:
      pass
  except:
    return None
    
  