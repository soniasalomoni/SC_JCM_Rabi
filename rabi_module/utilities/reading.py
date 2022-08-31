
import configparser
import sys
from sys import argv

sys.path.append('..')
import rabi_module as rabi

# define reading function

def read_txt():
    # initialize config 
    config = configparser.ConfigParser()

    # It is given the possibility to specify the configuration file as second argument in the bash command: sys.argv[1]  
    # The default configuration file if not specified through sys.argv[1] is "input.txt".

    if len(argv)>=2:
        config.read(argv[1])
    else:
        config.read("input.txt")

    # --------------------- #
    # initialize parameters #
    # --------------------- #

    AVG_N = int(config.get('field','avg_n'))
    PDF_N = config.get('field','pdf_n')
    CUT_N = int(config.get('field','cut_n'))

    Cg_0 = float(config.get('atom','Cg'))
    Ce_0 = float(config.get('atom','Ce'))

    OMEGA = float(config.get('interaction','int_coupling'))
    DELTA = float(config.get('interaction','int_detuning'))

    TMAX = int(config.get('simulation','time'))
    TSTEP = float(config.get('simulation','step'))

    SAVE_TXT = bool(config.get('output','save_txt'))
    SAVE_PNG = bool(config.get('output','save_png'))
    OUT_LABEL = config.get('output','out_label')

    # -------------------------- #
    # initialize class instances #
    # -------------------------- #

    field = rabi.Field(AVG_N,PDF_N,CUT_N)
    atom = rabi.Atom(Cg_0,Ce_0)
    system = rabi.System(field, atom, OMEGA, DELTA)
    simulation = rabi.Simulation(system,TMAX,TSTEP)

    saving_info = (SAVE_TXT, SAVE_PNG, OUT_LABEL)

    return simulation, saving_info