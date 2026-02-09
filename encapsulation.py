class InstagramAccount:
    def __init__(self, account_name, password):
        self.account_name = account_name
        self._private_reels = []
        self.__archived_reels = []
        # Important: password should be private → use __password
        self.__password = password

    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)
        print("Private Reel added:", reel_name)
        # Optional: print("Current private reels:", self._private_reels)

    def display_private_reels(self, is_follower):
        if is_follower:
            if not self._private_reels:
                print("No private reels yet.")
            else:
                print("Private Reels:")
                for reel in self._private_reels:
                    print("  •", reel)
        else:
            print("Access denied! Only followers can view private reels.")

    def add_archived_reel(self, reel_name):   # ← fixed method name (was add_archived_reels)
        self.__archived_reels.append(reel_name)
        print("Archived Reel added:", reel_name)

    def display_archived_reels(self, password):
        if password == self.__password:       # ← fixed: use self.__password
            if not self.__archived_reels:
                print("No archived reels.")
            else:
                print("Archived Reels:")
                for reel in self.__archived_reels:
                    print("  •", reel)
        else:
            print("Access Denied! Only account holder can view archived reels.")

    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels.copy()   # safer: return a copy
        else:
            print("Access denied - incorrect password")
            return None

    def set_password(self, old_password, new_password):
        if old_password == self.__password:    # ← fixed: was using self.password and self.__password
            if len(new_password) < 6:
                print("Error: New password must be at least 6 characters long.")
            else:
                self.__password = new_password
                print("Password updated successfully!")
        else:
            print("Incorrect old password.")

    # Optional: nice representation of the object
    def __str__(self):
        return f"Account: {self.account_name} | Private: {len(self._private_reels)} | Archived: {len(self.__archived_reels)}"




account = InstagramAccount('Ria', 'password123')

print(account)
print()

account.add_private_reel('reel1')
account.add_private_reel('dance-challenge')
account.add_archived_reel('reel2')
account.add_archived_reel('vacation-moments')



# Correct way to pass boolean (True/False – not string 'True')
account.display_private_reels(True)     # should show
account.display_private_reels(False)    # should deny



account.display_archived_reels('False')       # wrong password → denied
account.display_archived_reels('password123') # correct → should show



# Using getter
print("Archived reels via getter:")
print(account.get_archived_reels("password123"))



# Change password
print("Trying to change password:")
account.set_password("password123", "new_secure123")
account.set_password("wrong", "xyz")               # should fail

print("\nAfter password change:")
account.display_archived_reels("password123")      # should fail now
account.display_archived_reels("new_secure123")    # should work
