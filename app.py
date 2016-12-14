from flask import Flask, request, render_template
import os 
app = Flask(__name__)

@app.route('/')
def home():
	topadvs = os.listdir('static/images/topadvs')
	slideshow = os.listdir('static/images/slideshow') 
	#top_factor = len(topadvs)
	return render_template('home.html',
		topadvs=topadvs, 
		slideshow = slideshow,
		#top_factor=top_factor,

		)



if __name__ == "__main__":
	app.run(debug=True)