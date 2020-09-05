# palettable

### A simple program that creates a color palette for your images.

__________________________________________________________________
## Usage:

From your command line, clone the repository:<br>
`git clone https://github.com/ljsauer/palettable.git`
or, click on the green "Code" button at the top of the page and click "Download ZIP"<br>

Again from the command line, install the packages in requirements.txt:<br>
`pip install -r requirements.txt`<br>

Run the program, including a path to your image file:<br>
`python run.py -image <path/to/your/image>`<br>

Optionally, specify the position, orientation, and size of the palette. Example:<br>
`python run.py -image myimage.jpg -pos topLeft -orient vert -num 8`<br>

Output from above example:<br>
![Maple leaves](examples/maple.jpg "Maple leaves")