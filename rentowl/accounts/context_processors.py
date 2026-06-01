from accounts.forms import  Loginform,Registerform

def auth_forms(request):
    return {
        "loginform": Loginform(),
        "registerform": Registerform(),
    }