# -*- coding: utf-8 -*-
"""An awesome random number generator.

This module provides an implementation of the widely acclaimed RANDU random
number generator.

Example:
    This module is design to be included in your own Monte Carlo simulations
    but a simple example can be run from the command line by executing::

        $ python awesome-rng.py

    This will generate the default number of random numbers using the awesome
    default seed.

Attributes:
    LOGGER (int): Global logger. This guy will handle logs to the default
        log directory and to the console.

Todo:
    * Write RNG

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

from __future__ import print_function

import platform
import os
import datetime
import logging
import argparse

LOGGER = logging.getLogger(__name__)

SEED = 1
RNG_COUNT = 10

def init_awesome_rng(seed=SEED):
    """Function for initialising rng seed.
    This function can be used to initialise the seed for the random number
    generator. The seed MUST BE ODD.
    """
    global SEED  # Needed to be able to modify the global copy of SEED
    if seed % 2 == 1:
        SEED = seed
    else:
        raise ValueError('The awesome RNG seed must be an odd number.')

def awesome_rng():
    """Function for generating random numbers.
    This function uses the awesome RANDU algorithm to generate random numbers.
    You can specify your own seed and the number of random numbers to generate.
    """
    global SEED  # Needed to be able to modify the global copy of SEED
    SEED = 65539 * SEED % 2**31

    return SEED / 2**31

def awesome_rng_cli():
    """Command line interface to the awesome rng.
    This function will parse any command line arguments and launch a sample
    implementation of the random number generator.
    """
    parser = argparse.ArgumentParser(description="""A script for running a
                                                    the awesome-rng example.""")
    parser.add_argument("-n",
                        "--rng_count",
                        default=RNG_COUNT,
                        type=int,
                        help="Number of random numbers to generate.")
    parser.add_argument("-s",
                        "--seed",
                        default=SEED,
                        type=int,
                        help="An initial seed for the RNG.")
    args = parser.parse_args()

    LOGGER.info(" ")
    LOGGER.info("*********************************************")
    LOGGER.info("* AWESOME RNG                               *")
    LOGGER.info("*********************************************")
    LOGGER.info(" ")
    LOGGER.info("Input parameters are:")
    LOGGER.info(" ")
    LOGGER.info("-  Number of random numbers - %i", args.rng_count)
    LOGGER.info(" ")
    LOGGER.info("*********************************************")
    LOGGER.info(" ")

    try:
        init_awesome_rng(6)
    except ValueError:
        LOGGER.error("Seed must be an odd number.")
        raise

    rand_list = [awesome_rng() for r in range(args.rng_count)]

    LOGGER.info("Random number list - %s", repr(rand_list))

def set_up_logger():
    """This function initialises the logger.
    We set up a logger that prints both to the console at the information level
    and to file at the debug level. It will store in the /temp directory on
    *NIX machines and in the local directory on windows.
    """
    timestamp = datetime.datetime.now()

    logfile_name = 'awesome-rng-{0:04}-{1:02}-{2:02}-{3:02}{4:02}{5:02}.log'\
                   .format(timestamp.year,
                           timestamp.month,
                           timestamp.day,
                           timestamp.hour,
                           timestamp.minute,
                           timestamp.second)

    if platform.system() == 'Windows':
        if not os.path.exists('tmp'):
            os.makedirs('tmp')
        logfile_name = 'tmp/' + logfile_name
    else:
        logfile_name = '/tmp/' + logfile_name

    logging.basicConfig(filename=logfile_name,
                        level=logging.DEBUG)

    console_logger = logging.StreamHandler()
    console_logger.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console_logger.setFormatter(console_formatter)
    logging.getLogger('').addHandler(console_logger)

    LOGGER.info('All logging will be written to %s', logfile_name)

if __name__ == '__main__':
    set_up_logger()
    awesome_rng_cli()
