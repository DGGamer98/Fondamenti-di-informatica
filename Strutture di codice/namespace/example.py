x = "GLOBALE"

def function():
    global x #per renderla globale
    x = "LOCALE"
    print(x)

function()
print(x)