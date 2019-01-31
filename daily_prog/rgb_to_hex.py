"""
One common way for software specifications such as HTML to specify colors is with a hexadecimal string.
For instance the color aquamarine is represented by the string "#7FFFD4". Here's how the string breaks down:

The first character is always "#".

The second and third character are the red channel value, represented as a hexadecimal value between 00 and FF.
In this example, the red channel value is 127, which in hexadecimal is 7F.

The fourth and fifth character are the green channel value, represented the same way.
In this example, the green channel value is 255, which in hexadecimal is FF.

The sixth and seventh character are the blue channel value, represented the same way.
In this example, the blue channel value is 212, which in hexadecimal is D4.

All three channel values must be an integer between 0 (minimum brightness) and 255 (maximum brightness).
In all cases the hex values are two digits each, including a leading 0 if necessary.

See the Wikipedia page for more examples, and a link for how to convert a number to hexadecimal:
https://en.wikipedia.org/wiki/Web_colors#Converting_RGB_to_hexadecimal

Challenge:

Given three integers between 0 and 255, corresponding to the red, green, and blue channel values of a color,
find the hex string for that color. You may use anything built into your programming language,
such as for base conversion, but you can also do it manually.

"""

HEX_VALS = "0123456789ABCDEF"


def hexcolor(r, g, b):
    """
        Assuming valid ranges for r, g, b inputs, gives out a hex value.
    :param r: Int - range between 0 and 255
    :param g: Int - range between 0 and 255
    :param b: Int - range between 0 and 255
    :return: String - hex value of r, g, b.
    """
    r_h = str(HEX_VALS[r//16]) + str(HEX_VALS[r%16])
    g_h = str(HEX_VALS[g//16]) + str(HEX_VALS[g%16])
    b_h = str(HEX_VALS[b//16]) + str(HEX_VALS[b%16])
    return '#' + r_h + g_h + b_h


assert hexcolor(255, 99, 71) == "#FF6347"
assert hexcolor(184, 134, 11) == "#B8860B"
assert hexcolor(189, 183, 107) == "#BDB76B"
assert hexcolor(0, 0, 205) == "#0000CD"


def blend(hexes):
    """
        Assuming a list of appropriate hex values, returns the averaged result in rgb.
    :param hexes: List of hex values
    :return: Tuple (int, int, int) - tuple of r, g, b values of averaged given hex values.
    """
    if len(hexes) == 0:
        return False
    r = 0
    g = 0
    b = 0
    for i in range(len(hexes)):
        r += HEX_VALS.index(hexes[i][1]) * 16 + HEX_VALS.index(hexes[i][2])
        g += HEX_VALS.index(hexes[i][3]) * 16 + HEX_VALS.index(hexes[i][4])
        b += HEX_VALS.index(hexes[i][5]) * 16 + HEX_VALS.index(hexes[i][6])
    r = r // len(hexes)
    g = g // len(hexes)
    b = b // len(hexes)
    return hexcolor(r, g, b)


assert blend(["#000000", "#778899"]) == "#3B444C"
assert blend(["#E6E6FA", "#FF69B4", "#B0C4DE"]) == "#DCB1D9"


