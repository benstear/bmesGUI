#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 12:46:27 2018

@author: dawnstear
"""

''' DIMENSION REDUCTION CLASS '''
        
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn import (manifold, datasets, decomposition,
                     discriminant_analysis, random_projection)
import pandas as pd
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import scatter, figure, subplot, savefig
# if on jupyter lab/nb, uncomment: plt.switch_backend('agg')
from sklearn.utils import shuffle
import time
import os
#import umap
#import ZIFA

class DimensionReduction(object):
    
    def __init__(self,datamatrix, labels=None, shuffle=True, 
                 seed=None, dataset=None):

        self.X = datamatrix
        self.y = labels
        self.dataset = dataset
        self.cellcount = np.size(self.X,0)
        self.genecount = np.size(self.X,1)
        self.datasize = np.size(self.X)
        self.shuffle = shuffle
        
        # check for warnings that lda/etc wont work bc of some attribute of the dataset
        #
        #  good on 1078: pca/lle
    def plot2D(self,X,y,method,title,time_elapsed):
        fig, ax = plt.subplots()
        figure(figsize=(20, 20))
        ax.set(xlabel=method+' 1', ylabel=method+' 2',title = title)
        ax.legend(self.y)
        ax.scatter(self.X[:, 0], self.X[:, 1], c=self.y)
        #fig.savefig('/Users/dawnstear/desktop/Mid_Atlantic_Poster/tSNE_'+str(np.float16(time_elapsed))+'.png')
        fig.savefig('/scr1/users/stearb/results/plots_1078/'+method+'__'+str(np.float16(time_elapsed))+'.png')
        #fig.savefig('/users/stearb/desktop/myfig.png')    
        #os.mkdir('/scr1/users/stearb/results/plots_1078/')    

    def tsne(self,learning_rate=100):
        print('Calculating t-distributed stochastic neighbor embedding....\n')    
        start = time.time()
        tsne = TSNE(n_components=self.n_components,learning_rate=learning_rate)
        tsne_array = tsne.fit_transform(self.X)
        #plot2D(tsne_array,self.y,'t-SNE','t-SNE: 1078 cells with 10 cell subtypes',time.time() - start)
        tsne_params = tsne.get_params()
        return tsne_array

    def pca(self,n_components=2, solver='randomized'):
        print('Calculating PCA....\n')
        t = time.time()
        pca = PCA(n_components=n_components, svd_solver=solver)
        pca_array = pca.fit_transform(self.X) 
        #plot2D(pca_array,self.y,'PCA','PCA: 1078 cells with 10 cell subtypes', time.time() - t)
        return pca_array
    
    def lle(self, n_components=2,n_neighbors=20):
        print('Calculating local linear embedding....\n')
        start = time.time()
        lle = manifold.LocallyLinearEmbedding(n_neighbors=n_neighbors,n_components=n_components)
        lle_array = lle.fit_transform(self.X)
        #plot2D(lle_array,self.y,'LLE','Local Linear Embedding: 1078 cells with 10 cell subtypes',(time.time() - start))
        return lle_array
    
    def lda(self,n_components=2,solver='svd'):
        print('Calculating linear discriminant analysis....\n')
        t= time.time()
        lda = discriminant_analysis.LinearDiscriminantAnalysis(solver=solver,n_components=n_components)
        lda_array = lda.fit_transform(self.X, self.y)
        #plot2D(lda_array,self.y,'LDA','LDA: 1078 cells with 10 subtypes',(time.time() - t))
        return lda_array
    
    def isomap(self,n_components=2,solver='auto'):
        print('Calculating isomap....\n')
        t = time.time()
        iso = manifold.Isomap(n_neighbors=self.n_neighbors, n_components=n_components, eigen_solver=solver)
        iso_array = iso.fit_transform(self.X)
        #plot2D(iso_array,self.y,'isomap','Isomap: 1078 cells with 10 subtypes',time.time() - t)
        return iso_array
    
    def spectral(self,n_components=2):
        print('Calculating spectral embedding....\n')
        t = time.time()
        spectral = manifold.SpectralEmbedding(n_components=n_components, random_state=0)
        spectral_array = spectral.fit_transform(self.X) 
        #plot2D(spectral_array,self.y,'spectral','Spectral Embedding: 1078 cells with 10 subtypes',time.time() - t)
        return spectral_array
    
    def nnmf(self,n_components=2, init='random'):
        print('Calculating non-negative matrix factorization....\n')
        t =  time.time()
        nnmf = decomposition.NMF(n_components=n_components, init=init, random_state=0)
        nnmf_array = nnmf.fit_transform(self.X)
        #plot2D(nnmf_array,self.y,'nnmf','Non negative matrix factorization:\n1078 cells with 10 subtypes', time.time() - t)
        return nnmf_array


'''
################ UMAP ##############################
print('Calculating UMAP......')
t =  time.time()
umap_array = umap.UMAP().fit_transform(X)
time_elapsed = time.time() - t
plot2D(umap_array,y,'UMAP','Uniform Manifold Approximation and Projection:\n1078 cells with 10 subtypes',time_elapsed)


################ ZIFA ############################
from ZIFA import ZIFA
from ZIFA import block_ZIFA
k=2
print('Calculating ZIFA......')
t =  time.time()
#zifa_array, model_params = ZIFA.fitModel(X, k)
zifa_array, model_params = block_ZIFA.fitModel(X, k) #default blocksize is genes/500
time_elapsed = time.time() - t
plot2D(zifa_array,y,'ZIFA','Zero Inflated Dimensionality Reduction',time_elapsed)
'''
    
    