from flask import Flask


app = Flask(__name__)

# Home route
@app.route("/",methods = ['GET'])
def home():
    return "Welcome to GoToSchool"


#Main Logic
if __name__ == "__main__":
    # CORS(app)
    app.run(debug=True)