from data_manager import DataManager

def add_user():
    """
    Creates a new instance of DataManager and invokes the method to collect user data interactively.
    """
    
    new_user = DataManager(None) # We need to create a new item of the class DataManager but no need to give flight information
    new_user.collect_user_data()
    
if __name__ == "__main__":
    add_user()