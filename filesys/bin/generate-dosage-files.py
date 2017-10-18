#!/usr/bin/env python

'''
Generate random dosage files for use in lesson.
'''

import sys
import os
from getopt import getopt
import random
import string
from datetime import date, timedelta


MIN_DAYS = 10
MAX_DAYS = 50
MIN_DOSES = 1
MAX_DOSES = 20
MIN_DOSAGE = 1
MAX_DOSAGE = 25


def main():
    '''Main command-line driver.'''

    try:
        config = parseArgs()
        random.seed(config['seed'])
        patientIds = [genPatientId(config) for i in range(config['numPatients'])]
        checkPatientDirs(config, patientIds)
        for pid in patientIds:
            makePatientData(config, pid)
    except Exception as e:
        sys.stderr.write(str(e).rstrip() + '\n')
        sys.exit(1)


def parseArgs():
    '''Parse command-line arguments, returning config dictionary.'''

    config = {
        'dosageDir' : None,
        'endDate' : None,
        'force' : False,
        'numPatients' : None,
        'seed' : None,
        'startDate' : None,
        'verbose' : False
    }

    options, extras = getopt(sys.argv[1:], 'd:fn:r:vy:')
    if extras:
        raise Exception('Trailing arguments "{}"'.format(extras))

    for (opt, arg) in options:
        if opt == '-d':
            config['dosageDir'] = arg
        elif opt == '-f':
            config['force'] = True
        elif opt == '-n':
            config['numPatients'] = int(arg)
        elif opt == '-r':
            config['seed'] = int(arg)
        elif opt == '-v':
            config['verbose'] = True
        elif opt == '-y':
            config['year'] = int(arg)
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
    if (config['year'] < 2010) or (config['year'] > 2020):
        raise Exception('Year must be in 2010..2020 "{}"'.format(config['year']))

    return config


def genPatientId(config):
    '''Generate ID for a single patient.'''

    return ''.join([random.choice(string.ascii_uppercase) for i in range(2)]) + \
           ''.join([random.choice(string.digits) for i in range(4)])


def checkPatientDirs(config, patientIds):
    '''Check that patient directories can be created.'''

    dirs = [os.path.join(config['dosageDir'], p) for p in patientIds]
    failures = [d for d in dirs if os.path.exists(d)]
    if (not config['force']) and failures:
        raise Exception('Refusing to overwrite existing directories: {}'.format(', '.join(failures)))


def makePatientData(config, pid):
    '''Make data for patient.'''

    patientDir = os.path.join(config['dosageDir'], pid)
    os.mkdir(patientDir)
    start = date(config['year'], 1, 1)
    numSamples = random.randint(MIN_DAYS, MAX_DAYS)
    days = [(start + timedelta(days = d)).isoformat() for d in sorted(random.sample(range(365), numSamples))]
    for d in days:
        path = os.path.join(patientDir, d + '.csv')
        with open(path, 'w') as writer:
            makePatientDataFile(config, writer)


def makePatientDataFile(config, writer):
    '''Make data for a single patient on a single day.'''

    intervals = [10 * i for i in range(24 * 6)] # ten-minute intervals through the day
    numSamples = random.randint(MIN_DOSES, MAX_DOSES)
    times = ['{:02d}:{:02d}'.format(t//60, t%60) for t in random.sample(intervals, numSamples)]
    writer.write('Time,Dosage (mg)\n')
    for t in times:
        writer.write('{},{}\n'.format(t, 10 * random.randrange(MIN_DOSAGE, MAX_DOSAGE)))


if __name__ == '__main__':
    main()
