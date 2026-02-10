def admin_only(dashboard):
    def wrapper(username):
        if username == "admin":
            print("Access completed.")
            dashboard(username)
        else:
            print("Access denied.")
    return wrapper

@admin_only
def dashboard(username):
    print("Welcome to dashboard.")

dashboard("admin")
