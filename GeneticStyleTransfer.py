# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:23:30 2019

@author: Vishal Singh
@email: singhvishal0304@gmail.com
"""


import random
import numpy as np
import itertools
import functools
import operator

'''
function for finding gram matrix of a given matrix
'''
def gramMatrix(p):
	px=p.transpose(1,2,0).reshape(-1,p.shape[0])
	pt=np.transpose(px)
	gp=px.dot(pt)
	return gp
'''
fitness score is given by measuring error through euclidean distance between the gram matrices of population evolving
and target style image
'''

def fitness_score(gene_img ,style_im,img_shape):
	#This function transforms 1D matrix back to RGB image matrix
	gene_im= np.reshape(a=gene_img, newshape=img_shape)
	#print(gene_im.shape)
	gmContent=gramMatrix(gene_im)
	gmStyle=gramMatrix(style_im)
	#finding distance between the gram matrix of the genes and style image
	q1 = np.subtract(gmStyle,gmContent)
	#element-wise multiplication for squaring the error
	q2=np.multiply(q1,q1)
	fitness =np.mean(q2)
	return fitness
    
def survival_of_the_fittest(n_survived,current_gene,img_shape,style_im):
	#initializing an empty matrix for survival genes: no.ofrows=no. to survive
	
	survived= np.empty((n_survived, current_gene.shape[1]), dtype=np.uint8)
	maxerror=999999999999999999999999999999999999999999999999999
	#list to store fitness scores for genes
	fitness= np.zeros(current_gene.shape[0])
	#print(img_shape)
	for i in range(current_gene.shape[0]):
		fitness[i]=fitness_score(current_gene[i,:],style_im,img_shape)
	for i in range(n_survived):
		min_index = np.where(fitness == np.min(fitness))
		min_index= min_index[0][0]
		#storing survived genes
		survived[i, :] = current_gene[min_index, :]       
		#replacing with maximum error so that no gene is selected twice
		fitness[min_index]=maxerror
	return survived		       
        
        
'''
This function generates offspring equal to initial population- survived
'''
def breed(survived,n_gene,img_shape):
	
	
	new_genes = np.empty(shape=(n_gene, 
                                        functools.reduce(operator.mul, img_shape)),
                                        dtype=np.uint8)     
	new_genes[0:survived.shape[0], :] = survived
	# Getting how many offspring to be generated.
	n_offspring = n_gene-survived.shape[0]
	
	#  all possible permutations of the selected parents.
	survived_permutations = list(itertools.permutations(iterable=np.arange(0, survived.shape[0]), r=3)) 
        
	# Randomly selecting the parents permutations to generate the offspring.    
	selected_permutations = random.sample(range(len(survived_permutations)), 
                                          n_offspring)    
	comb_idx = survived.shape[0]
	for comb in range(len(selected_permutations)):
		
		first = np.int32(new_genes.shape[1]/3)
		second= 2*first
		selected_comb_idx = selected_permutations[comb]
		selected_comb = survived_permutations[selected_comb_idx]
		new_genes[comb_idx+comb, 0:first] = survived[selected_comb[0], 
	                                                             0:first]
		new_genes[comb_idx+comb, first:second] = survived[selected_comb[1], 
	                                                             first:second]
	       
	        
		new_genes[comb_idx+comb, second:] = survived[selected_comb[2], 
	                                                             second:]
		
	    			       
		        
		        
		       #pivot is selected as the 1/3rd and 2/3rd of the population after which elements are exchanged
		
	        # Generating the offspring using the permutations previously selected randmly.
		       
			
		              
		        
	return new_genes   	                   		   
''''
Mutation enables offsprings to deviate from the characteristics of parent genes
'''               
	
def mutation(population,num_parents_mating, mut_percent):
	for i in range(num_parents_mating, population.shape[0]):
		#implementation inspired by project GARI by Ahmed F. Gad.
		# A predefined percent of genes are selected randomly.
	        rand_idx = np.uint32(np.random.random(size=np.uint32(mut_percent/100*population.shape[1]))
	                                                    *population.shape[1])
	        # Changing the values of the selected genes randomly.
	        new_values = np.uint8(np.random.random(size=rand_idx.shape[0])*256)
	        # Updating population after mutation.
	        population[i, rand_idx] = new_values
	return population   


    
        
    
	    
    
    
    
   
	   
	   

   
   



