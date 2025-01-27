import os
print(os.getcwd())  # Print the current working directory

from app import create_app 

app = create_app()  # Initialize the app using the create_app function

if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode for development
