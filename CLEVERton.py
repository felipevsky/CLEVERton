import pyAIML

# The Kernel object is the public interface to the AIML interpreter.
k = pyAIML.Kernel()

# Use the 'learn' method to load the contents of an AIML file into the Kernel.
k.learn("startup.xml")

# Use the 'respond' method to compute the response
# to a user's input sring. respond() returns the
# interpreter's response, which in this case we
# ignore
k.respond("load aiml cn")

# Loop forever, reading user input from the command
# line and printing respones
while True: print k.respond(raw_input("> "))
