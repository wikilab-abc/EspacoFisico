TARGETS = ui_MainWindow.py ui_cadastroPessoas.py ui_DlgEspacoFisico.py

all: ${TARGETS}

ui_MainWindow.py: MainWindow.ui
	pyuic5 $< > $@
ui_cadastroPessoas.py: cadastroPessoas.ui
	pyuic5 $< > $@
ui_DlgEspacoFisico.py: DlgEspacoFisico.ui
	pyuic5 $< > $@

.PHONY: clean
clean:
	rm -f ${TARGETS}
	rm -rf __pycache__
