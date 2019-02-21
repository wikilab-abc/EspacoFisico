TARGETS = ui_mainwindow.py

all: ${TARGETS}

ui_mainwindow.py: mainwindow.ui
	pyuic5 $< > $@

.PHONY: clean
clean:
	rm -f ${TARGETS}
	rm -rf __pycache__
