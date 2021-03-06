#!/usr/bin/env python
# coding=utf-8
from IOinterface import *
from classes import *
from build_complex4 import *
from energies import *

prots_files = get_input_file(options.input_directory)

get_output_file(options.output_directory, options.force)



chain_list, nomen = all_chains(prots_files, options.verbose)

int_dict = get_interactions_dict(chain_list, prots_files, options.verbose, options.template)

n = 0
filenames = []
while n < int(options.models):
	if options.template is not None:
		if options.verbose:
			print("Starting the construction of model %s"%(n+1))
		model = template_loop(chain_list, int_dict, nomen, options.template, options.output_directory, options.verbose, options. stechiometry)
	else:
		if options.verbose:
			print("Starting the construction of model %s"%(n+1))
		model = main_loop(chain_list, int_dict, nomen, options.verbose, options. stechiometry)
	filename = save_PDB(model, options.output_directory, n+1, options.verbose)
	filenames.append(filename)
	n += 1

if options.energy:
	for file in filenames:
		if options.verbose:
			print("Calculating DOPE score of %s"%file)
		energy = DOPE_Energy(file, options.output_directory, options.verbose)
