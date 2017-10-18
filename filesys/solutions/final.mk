STEMS=$(notdir $(wildcard dosage/*))
DAILY=$(patsubst %,daily/%.csv,${STEMS})

averages.csv : ${DAILY}
	bin/patient-average -o $@ ${DAILY}

daily/%.csv : dosage/%/*.csv
	mkdir -p daily
	bin/patient-total -o $@ $^
