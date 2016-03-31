# sagerbingo
A python module to play Sager Bingo during Unsupervised Learning and Time Series Analysis!

The module creates an object called Board. Board has several attributes and methods but the main onces you need to know are .board, .square_options, .shuffle(), .X(col,row) and .un_X(col,row).

See the example IPython notebook and feel free to use that notebook to play today. Let me know of any you run into as you go!

# Installation instructions
I'd reccoemend running on Python 2.7 (since I know some people are still using that in the program), if you only have 3.5 learn virtual environments- it's safer to try new code in a virtual environmemnt.

You'll need standard things, Numpy, Pandas, IPython.

To install run the setup.py from the package directory:

```
python setup.py install
```

After that it should be fully operational