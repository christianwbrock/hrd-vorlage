from .stars import get_star_list


def main():
    print_star_table("star_table.tex")




def print_star_table(filename):
    stars = get_star_list()

    with open(filename, "w") as f:
        f.write(r"""
\begin{tabular}{llll}
\toprule
Name & Temperature (K) & Brightness (abs.\ mag) & Type \\
""")
        for i, star in enumerate(stars):

            if i % 5 == 0:
                f.write(r"\midrule")
                f.write("\n")

            f.write(rf"{star.name} & {star.temp} & {star.mag} & {star.description} \\")
            f.write("\n")

        f.write(r"""
\bottomrule        
\end{tabular}
""")
