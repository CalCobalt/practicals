def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def convert_file(input_file="prac_03/temps_input.txt", output_file="prac_03/temps_output.txt"):
    fin = open(input_file, "r")
    fout = open(output_file, "w")

    for line in fin:
        try:
            f_value = float(line.strip())
            c_value = fahrenheit_to_celsius(f_value)
            fout.write(str(c_value) + "\n")
        except ValueError:
            print("Skip:", line.strip())

    fin.close()
    fout.close()

def main():
    convert_file()
    print("Done! temps_output.txt created.")

main()