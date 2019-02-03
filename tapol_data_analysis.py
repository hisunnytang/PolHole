# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 23:25:39 2014

@author: Sunny Tang
"""
from astropy.io import fits
import numpy
import matplotlib.pyplot as plt
import pyfits


def main():
    directory = 'C:\\Users\\Sunny Tang\\Desktop\\Polarization Hole\\Observation\\CARMA TAPOL\\'

    source_all = ['f4\\W3Main','f5\\W3OH','f6\\L1448I','f7\\L1448N','f8\\L1448C','f9\\L1445','f10\\IRAS2A','f11\\SVS13','f12\\IRAS4A','f13\\IRAS4B','f14\\HH211','f15\\DGTau','f16\\L1551','f17\\L1527','f18\\CB26','f19\\OrionKL','f20\\MMS6','f21\\FIR4','f23\\VLA1623','f24\\SerEmb17','f26\\SerEmb8','f27\\SerEmb6','f31\\B335','f32\\DR21OH','f33\\L1157', 'f34\\CB230']
    
    
    dir_Ico = '.co.I.cm.fits'
    dir_Idust = '.dust.I.cm.fits'
    dir_pFrac = '.dust.pfrac.fits'
    dir_pa = '.dust.pa.fits'
    
    dir_Main_Tapol = '_vectors.log'
    dir_Main_others = '_vectors_bolo.log'

    tapol_m =[]
    tapol_sd = []
    tapol_l =[]
    scuba_m = []
    scuba_sd = []
    scuba_l = []
    hertz_m = []    
    hertz_sd = []
    hertz_l = []
    sharp_m =[]
    sharp_sd =[]
    sharp_l = []    
    
    label = [ i[3:] for i in source_all[:6]] + [j[4:] for j in source_all[6:]]
    
    for i in range(len(source_all)):
        source = source_all[i]
        tapol_m,tapol_sd,tapol_l,scuba_m,scuba_sd,scuba_l,hertz_m,hertz_sd,hertz_l,sharp_m,sharp_sd,sharp_l = take_data(source,tapol_m,tapol_sd,tapol_l,scuba_m,scuba_sd,scuba_l,hertz_m,hertz_sd,hertz_l,sharp_m,sharp_sd,sharp_l)
    plt.subplots(figsize=(20,20))
    for i in range(len(source_all)):
        if tapol_l[i]>10:
            if scuba_l[i]!=0:
                if hertz_l[i]>10:
                    plt.scatter(1+i/40.0,tapol_m[i])
                    plt.annotate(label[i]+' '+str(tapol_l[i]),xy = (1+i/40.0,tapol_m[i]))
                    plt.scatter(2+i/40.0,scuba_m[i])
                    plt.annotate(label[i]+' '+str(scuba_l[i]),xy = (2+i/40.0,scuba_m[i]))
                    plt.scatter(3+i/40.0,hertz_m[i])
                    plt.plot([1+i/40.0,2+i/40.0,3+i/40.0],[tapol_m[i],scuba_m[i],hertz_m[i]])
                    plt.annotate(label[i]+' '+str(hertz_l[i]),xy = (3+i/40.0,hertz_m[i]))
                    
                if sharp_l[i]>10:
                    plt.scatter(1+i/40.0,tapol_m[i])
                    plt.annotate(label[i]+' '+str(tapol_l[i]),xy = (1+i/40.0,tapol_m[i]))
                    plt.scatter(2+i/40.0,scuba_m[i])
                    plt.annotate(label[i]+' '+str(scuba_l[i]),xy = (2+i/40.0,scuba_m[i]))
                    plt.scatter(3+i/40.0,sharp_m[i])
                    plt.plot([1+i/40.0,2+i/40.0,3+i/40.0],[tapol_m[i],scuba_m[i],sharp_m[i]])
                    plt.annotate(label[i]+' '+str(sharp_l[i]),xy = (3+i/40.0,sharp_m[i]))

        

            
    plt.savefig('chaotic_one.pdf')
    
    return tapol_m,tapol_sd,tapol_l,scuba_m,scuba_sd,scuba_l,hertz_m,hertz_sd,hertz_l,sharp_m,sharp_sd,sharp_l    
    
def take_data(source,tap_m,tap_sd,tap_l,scu_m,scu_sd,scu_l,her_m,her_sd,her_l,sha_m,sha_sd,sha_l):
    directory = 'C:\\Users\\Sunny Tang\\Desktop\\Polarization Hole\\Observation\\CARMA TAPOL\\'
    dir_Ico = '.co.I.cm.fits'
    dir_Idust = '.dust.I.cm.fits'
    dir_pFrac = '.dust.pfrac.fits'
    dir_pa = '.dust.pa.fits'
    
    dir_Main_Tapol = '_vectors.log'
    dir_Main_others = '_vectors_bolo.log'

    try:
        with open(directory+source+dir_Main_Tapol,'r') as f:
            raw = f.readlines()
        raw = raw[29:]
    except:
        raw = []
    try:
        with open(directory+source+dir_Main_others,'r') as f:
            raw1 = f.readlines()
        raw1 = raw1[33:]
    except:
        raw1 = []
        
    l = len(raw)
    j = 0
    k = 0
    new = range(l)
    new1 = range(len(raw1))
    new_scuba = []
    new_hertz = []
    new_sharp = []
    tmp1 = 'SCUBA'
    tmp2 = 'Hertz'
    

    
    if raw!=[]:
        for i in raw:
            new[j] = map(float,i.split())
            j = j + 1
        tapol = numpy.transpose((numpy.array(new)))
        tap_m.append(numpy.average(tapol[4]))
        tap_sd.append(numpy.std(tapol[4]))
        tap_l.append(len(tapol[4]))
        with open("tapol.txt", "a") as myfile:
            myfile.write(str(numpy.average(tapol[4])) +' ' + str(numpy.std(tapol[4]))+'\n')
    else:
        with open("tapol.txt", "a") as myfile:
            myfile.write(str(0) +' ' + str(0)+'\n')
        tap_m.append(0)
        tap_sd.append(0)
        tap_l.append(0)
    if raw1!=[]:     
        for i in raw1:
            new1[k] = i.split()
            if new1[k][7] == tmp1:
                new_scuba.append(map(float,new1[k][:6]))
            elif new1[k][7] == tmp2:
                new_hertz.append(map(float,new1[k][:6]))
            else:
                new_sharp.append(map(float,new1[k][:6]))
        scuba = numpy.transpose(numpy.array(new_scuba))
        hertz = numpy.transpose(numpy.array(new_hertz))
        sharp = numpy.transpose(numpy.array(new_sharp))
    else:
        scuba=[]
        hertz=[]
        sharp=[]
        
    if scuba!=[]:
        with open("scuba.txt", "a") as myfile:
            myfile.write(str(numpy.average(scuba[3])) +' ' + str(numpy.std(scuba[3]))+ '\n')
        scu_m.append(numpy.average(scuba[3]))
        scu_sd.append(numpy.std(scuba[3]))
        scu_l.append(len(scuba[3]))
    else:
        with open("scuba.txt","a") as myfile:
            myfile.write(str(0)+' ' +str(0)+'\n')
        scu_m.append(0)
        scu_sd.append(0)
        scu_l.append(0)
    if hertz!=[]:
        with open("hertz.txt", "a") as myfile:
            myfile.write(str(numpy.average(hertz[3])) +' ' + str(numpy.std(hertz[3]))+ '\n')
        her_m.append(numpy.average(hertz[3]))
        her_sd.append(numpy.std(hertz[3]))
        her_l.append(len(hertz[3]))
    else:
        with open("hertz.txt","a") as myfile:
            myfile.write(str(0)+' ' +str(0)+'\n')    
        her_m.append(0)
        her_sd.append(0)
        her_l.append(0)
    if sharp!=[]:
        with open("sharp.txt", "a") as myfile:
            myfile.write(str(numpy.average(sharp[3])) +' ' + str(numpy.std(sharp[3]))+ '\n')
        sha_m.append(numpy.average(sharp[3]))
        sha_sd.append(numpy.std(sharp[3]))
        sha_l.append(len(sharp[3]))
    else:
        with open("sharp.txt","a") as myfile:
            myfile.write(str(0)+' ' +str(0)+'\n')
        sha_m.append(0)
        sha_sd.append(0)
        sha_l.append(0)
    return tap_m,tap_sd,tap_l,scu_m,scu_sd,scu_l,her_m,her_sd,her_l,sha_m,sha_sd,sha_l  