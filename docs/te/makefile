all:
	latex memte.tex
	latex memte.tex
	bibtex memte
	latex memte.tex
	latex memte.tex
	dvips -o memte.ps memte.dvi
	ps2pdf -sPAPERSIZE=a4 -DMaxSubsetPct=100 -dCompatibilityLevel=1.2 -dSubsetFonts=true -dEmbedAllFonts=true memte.ps memte.pdf

clean:
	rm -f *.toc *.ps *.log *.lof *.lot *.dvi *.aux *.blg *.bbl
