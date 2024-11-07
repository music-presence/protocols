.PHONY: all setup clean-build rebuild-py clean-dist gen

all:

bin/protoc-gen-jsonschema:
	git submodule update --init --recursive
	mkdir -p bin
	cd third_party/protoc-gen-jsonschema &&\
		go build -o ../../bin/protoc-gen-jsonschema ./main.go

build/py: bin/protoc-gen-jsonschema
	mkdir -p build/py
	protoc \
		--python_out=build/py \
		-I ./third_party/protoc-gen-jsonschema \
		-I ./src \
		./src/*.proto \
		./third_party/protoc-gen-jsonschema/jsonschema.proto

.venv:
	python -m venv .venv &&\
		source ./.venv/Scripts/activate &&\
		python -m pip install -U pip &&\
		python -m pip install -r requirements.txt

setup: bin/protoc-gen-jsonschema build/py .venv

clean-build:
	rm -rf build

rebuild-py: clean-build build/py

clean-dist:
	rm -rf dist

gen: clean-dist rebuild-py
	mkdir -p dist/schemas
	inv gen
