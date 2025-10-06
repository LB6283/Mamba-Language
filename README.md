 Mamba Documentation:


Mamba is a programming language designed to offer a customizable, Python-like user experience. One thing I think is cool about this "language" is that you can change the declaration of each function so that it behaves however you want! It is open source. Please give any input you have!


out(*args, **kwargs):
prints everything in tuple args. Uses keyword arguments from the dictionary kwargs to define certain parameters.
Keyword arguments:
spaceing: the spaceing keyword argument defines the amount of space between each arg in args.
Endspace: the endspace keyword determines whether the amount of spacing set by the spaceing keyword should apply to the final argument. Default is True. 
end_spaceing: if endspace is set to False, then you can set a specific value for the spacing after the final argument in arg.
End: the end keyword argument defines what the function will do after it has printed every arg in args; default is ‘\n’.


accept(*args, **kwargs):
The accept function accepts user input.
Prints all arguments in the tuple args.
Keyword Arguments:
cursor_position: The cursor_position keyword argument determines where the user’s cursor will be with respect to the text default is an empty string.
All other keyword arguments serve the same purpose as they do in the out() function.

I will try to update this as often as I can and add notes to my Python programs.
