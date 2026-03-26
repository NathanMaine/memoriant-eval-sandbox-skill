ROOT_DIR := $(abspath $(CURDIR)/..)

.PHONY: venv install test run

venv:
	$(MAKE) -C $(ROOT_DIR) venv

install:
	$(MAKE) -C $(ROOT_DIR) install

test:
	$(MAKE) -C $(ROOT_DIR) test

run:
	$(MAKE) -C $(ROOT_DIR) run-aes
