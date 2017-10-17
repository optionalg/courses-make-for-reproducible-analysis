#!/usr/bin/env python

'''
Generate random dosage files for use in lesson.
'''

import sys
import os
from getopt import getopt

def main():
    '''Main command-line driver.'''

    try:
        config = parseArgs()
        for patientNum in range(config['numPatients']):
            makePatientData(config)
    except Exception as e:
        sys.stderr.write(str(e).rstrip() + '\n')
        sys.exit(1)


def parseArgs():
    '''Parse command-line arguments, returning config dictionary.'''

    config = {
        'dosageDir' : None,
        'numPatients' : None,
        'seed' : None,
        'verbose' : False
    }

    options, extras = getopt(sys.argv[1:], 'd:n:r:v')
    if extras:
        raise Exception('Trailing arguments "{}"'.format(extras))

    for (opt, arg) in options:
        if opt == '-d':
            config['dosageDir'] = arg
        elif opt == '-n':
            config['numPatients'] = int(arg)
            pass
        elif opt == '-r':
            config['seed'] = int(arg)
            pass
        elif opt == '-v':
            config['verbose'] = True
        else:
            raise Exception('Unrecognized option "{}"'.format(opt))

    if config['dosageDir'] is None:
        raise Exception('Dosage directory not configured (use -d)')
    if not os.path.isdir(config['dosageDir']):
        raise Exception('Dosage directory "{}" does not exist'.format(config['dosageDir']))
    if config['numPatients'] is None:
        raise Exception('Number of patients not configured (use -n)')
    if config['numPatients'] <= 0:
        raise Exception('Number of patients must be positive "{}"'.format(config['numPatients']))
    if config['seed'] is None:
        raise Exception('RNG seed not configured (use -r)')
    if config['seed'] <= 0:
        raise Exception('RNG seed must be positive "{}"'.format(config['seed']))

    return config


def makePatientData(config):
    '''Generate data for a single patient.'''

    pass


if __name__ == '__main__':
    main()
