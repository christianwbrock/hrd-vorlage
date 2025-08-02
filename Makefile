
all:: science_astronomy_hrd.pdf

science_astronomy_hrd.pdf: science_astronomy_hrd.tex hrd_with_stars.png hrd_empty.png star_table.tex
	pdflatex science_astronomy_hrd.tex
	pdflatex science_astronomy_hrd.tex

clean::
	$(RM) *.aux *.log *.out *.toc *.bbl *.blg *.dvi *.synctex.gz

mrproper:: clean
	$(RM) science_astronomy_hrd.pdf


hrd_with_stars.png:
	hrd_plot_full_hrd

mrproper::
	$(RM) hrd_with_stars.png

hrd_empty.png:
	hrd_plot_empty_hrd

mrproper::
	$(RM) hrd_empty.png

star_table.tex:
	hrd_star_table

clean::
	$(RM) star_table.tex
