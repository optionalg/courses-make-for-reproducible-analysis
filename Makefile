FILESYS=./filesys
DOSAGE_DIR=${FILESYS}/dosage
NUM_PATIENTS=20
SEED=7493418

# default target
all : commands

## commands   : show all commands.
commands :
	@grep -E '^##' Makefile | sed -e 's/## //g'

## dosage     : regenerate raw dosage files.
dosage :
	bin/generate-dosage-files.py -d ${DOSAGE_DIR} -n ${NUM_PATIENTS} -r ${SEED}

design/concept.svg : design/concept.dot
	dot -Tsvg -odesign/concept.svg design/concept.dot
