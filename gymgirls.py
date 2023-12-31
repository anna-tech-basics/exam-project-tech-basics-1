
# removed class
# replaced self with root
# adjusted commands


import tkinter as tk
# from PIL import Image, ImageTk


root = tk.Tk()
root.title("GymGirls")
root.geometry("400x500")



def create_first_frame(root):
    # setting background to black
    # grid method to specify position, sticky="nsew" allows frame to fill space
    root.first_frame = tk.Frame(root, bg="black")
    root.first_frame.grid(row=0, column=0, sticky="nsew")
    # Widgets for the first frame
    # creates username and password label
    # sets font
    # creates entry boxes for username and password
    # grid() method to position widgets
    # padx and pady adds padding
    label_username = tk.Label(root.first_frame, text="Username:", fg="white", font=("Helvetica", 12), bg="black")
    label_username.grid(column=0, row=3, padx=10, pady=10)

    entry_username = tk.Entry(root.first_frame)
    entry_username.grid(column=1, row=3, padx=10, pady=10)

    label_password = tk.Label(root.first_frame, text="Password:", fg="white", font=("Helvetica", 12), bg="black")
    label_password.grid(column=0, row=4, padx=10, pady=10)

    # shows * instead of letters for password
    entry_password = tk.Entry(root.first_frame, show="*")
    entry_password.grid(column=1, row=4, padx=10, pady=10)

    # Creates a button widget to join and a command to execute when clicked
    join_button = tk.Button(root.first_frame, text="Join GymGirls", command=lambda: on_join_clicked(root))
    join_button.grid(column=0, row=5, columnspan=2, pady=10)

def on_join_clicked(root):
    # Destroys the first frame
    root.first_frame.destroy()

    # Creates and displays the new frame
    create_main_frame(root)

# creates main frame
def create_main_frame(root):
    root.main_frame = tk.Frame(root, bg="#FFE1FF")
    root.main_frame.grid(row=0, column=0, sticky="nsew")

    # Configures column and row weights
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Widgets for the main frame
    label_welcome = tk.Label(root.main_frame, text="Welcome to GymGirls!", font=("Helvetica", 16))
    label_welcome.grid(column=0, row=0, columnspan=2, sticky="nsew")

    profile_button = tk.Button(root.main_frame, text="Create Profile", command=lambda: open_profile_frame(root))
    profile_button.grid(column=0, row=1, columnspan=2, pady=10, sticky="ew")

# defines what happens when create profile is clicked
def open_profile_frame(root):
    # Destroys the main frame
    root.main_frame.destroy()
    # Creates the profile frame
    root.profile_frame = tk.Frame(root, bg="white")
    root.profile_frame.grid(row=0, column=0, sticky="nsew")

    # Configure column and row weights
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Widgets for the profile frame
    label_profile = tk.Label(root.profile_frame, text="Create Your Profile", font=("Helvetica", 16))
    label_profile.grid(column=0, row=0, columnspan=2, sticky="nsew")

    # Add profile labels and input fields
    label_name = tk.Label(root.profile_frame, text="Name:")
    label_name.grid(column=0, row=1, padx=10, pady=10, sticky="w")

    entry_name = tk.Entry(root.profile_frame)
    entry_name.grid(column=1, row=1, padx=10, pady=10, sticky="ew")

    label_age = tk.Label(root.profile_frame, text="Age:")
    label_age.grid(column=0, row=2, padx=10, pady=10, sticky="w")

    entry_age = tk.Entry(root.profile_frame)
    entry_age.grid(column=1, row=2, padx=10, pady=10, sticky="ew")

    label_membership = tk.Label(root.profile_frame, text="Gym Membership:")
    label_membership.grid(column=0, row=3, padx=10, pady=10, sticky="w")

    #  dropdown menu for membership status
    # reference https://www.geeksforgeeks.org/dropdown-menus-tkinter/
    membership_options = ["Yes", "No"]
    var_membership = tk.StringVar(root.profile_frame)
    var_membership.set(membership_options[0])  # Default value
    dropdown_membership = tk.OptionMenu(root.profile_frame, var_membership, *membership_options)
    dropdown_membership.grid(column=1, row=3, padx=10, pady=10, sticky="ew")

    label_gym = tk.Label(root.profile_frame, text="if yes which one:")
    label_gym.grid(column=0, row=4, padx=10, pady=10, sticky="w")

    entry_gym = tk.Entry(root.profile_frame)
    entry_gym.grid(column=1, row=4, padx=10, pady=10, sticky="ew")

    label_goals = tk.Label(root.profile_frame, text="Fitness Goals:")
    label_goals.grid(column=0, row=5, padx=10, pady=10, sticky="w")

    entry_goals = tk.Entry(root.profile_frame)
    entry_goals.grid(column=1, row=5, padx=10, pady=10, sticky="ew")

    label_partner = tk.Label(root.profile_frame, text="Looking for a Gym Partner:")
    label_partner.grid(column=0, row=6, padx=10, pady=10, sticky="w")

    # dropdown menu for partner preference
    partner_options = ["Yes", "No"]
    var_partner = tk.StringVar(root.profile_frame)
    var_partner.set(partner_options[0])
    dropdown_partner = tk.OptionMenu(root.profile_frame, var_partner, *partner_options)
    dropdown_partner.grid(column=1, row=6, padx=10, pady=10, sticky="ew")

    # Adds a button to save the profile
    save_button = tk.Button(root.profile_frame, text="Save Profile", command=lambda: save_profile(root))
    save_button.grid(column=0, row=7, columnspan=2, pady=10, sticky="ew")

# defines what happens when save profile is clicked
def save_profile(root):
    # destroys profile frame
    root.profile_frame.destroy()
    # creates profile saved frame
    root.saved_profile = tk.Frame(root, bg="white")
    root.saved_profile.grid(row=0, column=0, sticky="nsew")

    # widgets for profile saved frame
    label_saved_profile = tk.Label(root.saved_profile, text="Profile Saved!", font=("Helvetica", 20))
    label_saved_profile.grid(column=2, row=2, columnspan=2, sticky="nsew")

    button_getstarted = tk.Button(root.saved_profile, text="Get started", font=("Helvetica", 22), command=lambda: get_started(root))
    button_getstarted.grid(column=4, row=6, columnspan=2, sticky="nsew")

# defines what happens when get started is clicked
def get_started(root):
    root.saved_profile.destroy()
    # Recreates the main frame
    root.main_frame = tk.Frame(root, bg="#FFE1FF")
    root.main_frame.grid(row=0, column=0, sticky="nsew")

    # Configure column and row weights
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Widgets for the main frame
    label_welcome = tk.Label(root.main_frame, text="Hi GymGirl!", font=("Helvetica", 16))
    label_welcome.grid(column=0, row=0, columnspan=2, sticky="nsew")

    # Adds buttons for different actions
    share_training_button = tk.Button(root.main_frame, text="Share Your Training", command=lambda: share_training(root))
    share_training_button.grid(column=0, row=1, columnspan=2, pady=10, sticky="ew")

    connect_button = tk.Button(root.main_frame, text="Connect with Gym Girls at Your Gym", command=lambda: connect_with_gym_girls(root))
    connect_button.grid(column=0, row=2, columnspan=2, pady=10, sticky="ew")

    find_gyms_button = tk.Button(root.main_frame, text="Find Gyms with Women-only Options", command=lambda: find_women_only_gyms(root))
    find_gyms_button.grid(column=0, row=3, columnspan=2, pady=10, sticky="ew")

    share_experiences_button = tk.Button(root.main_frame, text="Share Experiences", command=lambda: share_experiences(root))
    share_experiences_button.grid(column=0, row=4, columnspan=2, pady=10, sticky="ew")

def share_training(root):
    # room for future enhancement
    pass

def connect_with_gym_girls(root):
    # room for future enhancement
    pass

def find_women_only_gyms(root):
    # room for future enhancement
    pass

def share_experiences(root):
    # room for future enhancement
    pass


create_first_frame(root)

root.mainloop()
