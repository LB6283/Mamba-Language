from lang import *

variables.declare("x", Num(6.7))
variables.declare("y", Num(4))
variables.declare("z", sum(variables.fetch("x"), variables.fetch("y")))

out(variables.fetch("z"))

