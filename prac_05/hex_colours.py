colors = {
  "Absolute Zero": "#0048ba",
  "Acid Green": "#b0bf1a",
  "AliceBlue": "#f0f8ff",
  "Alizarin crimson": "#e32636",
  "Amaranth": "#e52b50",
  "Amber": "#ffbf00",
  "Amethyst": "#9966cc",
  "AntiqueWhite": "#faebd7",
  "AntiqueWhite1": "#ffefdb",
  "AntiqueWhite2": "#eedfcc",
  "YellowGreen": "#9acd32",
  "Zaffre": "#0014a8",
  "Zomp": "#39a78e"
}

def main():
    while True:
        colour_name = input("input color: ").strip()
        if colour_name == "":
            break
        code = colors.get(colour_name.title())
        if code:
            print(f"{colour_name.title()} : {code}")
        else:
            print("retry")

main()