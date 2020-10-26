# CS323-Project
Artificial Intelligence Project 

This project is inspired from [Physical Gradient Descent repository](https://github.com/chrisfosterelli/physical-gradient-descent) and this [blog post](https://fosterelli.co/executing-gradient-descent-on-the-earth)

The goal of the project is to - 

Get the location of a nearby hill wherever our starting conditions are. For simplicity the starting location is taken to be the Indian Institute of Technology, Jodhpur with latitude `26.472258` and longitude `73.115067`.

##Getting Started 

- Python3 should be pre-installed and install the dependencies with the following commands-
```
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
``` 
- Run `python main.py` to get the output files. Note that this command should be run in the same terminal window. This command will show a graph plotted for different algorithms. It can be safely closed after viewing. 
- Run `python -m http.server` to serve the files locally. Go to http://localhost:8000 to check the files. Select `visualizer.html` to see the virtualized data. 

##Advanced Usage

- Open `args.json` to get get the global arguments being used in the project. The different arguments can be changed according to need.
- However while changing `lat` and `long` near the jodhpur area. If a area outside is to be used the `GeoTIFF` file as to be changed in the `tifs` directory. Replace this with the appropriate file from http://dwtkns.com/srtm/ and make the corresponding changes to `args.json`.  