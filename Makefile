TARGETS = ui_mainwindow.py ui_cadastroPessoas.py ui_DlgEspacoFisico.py

all: ${TARGETS}

ui_mainwindow.py: mainwindow.ui
	pyuic5 $< > $@
ui_cadastroPessoas.py: cadastroPessoas.ui
	pyuic5 $< > $@
ui_DlgEspacoFisico.py: DlgEspacoFisico.ui
	pyuic5 $< > $@

.PHONY: clean
clean:
	rm -f ${TARGETS}
	rm -rf __pycache__
