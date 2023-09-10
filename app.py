from flask import Flask, render_template, request
import pyshorteners

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
          short_url = ""
          
          if request.method == "POST":
            long_url = request.form["input"]
            try:
                  convert_short = pyshorteners.Shortener()
                  short_url = convert_short.tinyurl.short(long_url)
            except Exception as e:
                  error = e
                  print(e)
                  return render_template("index.html", url=short_url, error=error)
            
          return render_template("index.html", url=short_url)

if __name__ == "__main__":
      app.run(debug=True, port=6969)