python3=python3
venv_dir=venv

html: $(venv_dir)/packages-installed
	$(venv_dir)/bin/sphinx-build -M html . _build $(SPHINXOPTS)

open:
	make html
	open _build/html/index.html

clean:
	rm -rf _build

$(venv_dir)/packages-installed: requirements.txt
	test -d $(venv_dir) || $(python3) -m venv $(venv_dir)
	$(venv_dir)/bin/pip install -U pip wheel
	$(venv_dir)/bin/pip install -r requirements.txt
	touch $@


# # Minimal makefile for Sphinx documentation
# #
#
# # You can set these variables from the command line, and also
# # from the environment for the first two.
# SPHINXOPTS    ?=
# SPHINXBUILD   ?= sphinx-build
# SOURCEDIR     = .
# BUILDDIR      = _build
#
# # Put it first so that "make" without argument is like "make help".
# help:
# 	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
#
# .PHONY: help Makefile
#
# # Catch-all target: route all unknown targets to Sphinx using the new
# # "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
# %: Makefile
# 	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
