# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 14:10:40 2014

@author: Cloudy Tang
"""

from astropy.io import fits
import numpy
import matplotlib.pyplot as plt
import a


def Bdisp_vs_deg():
    
    source_all = ['f4\\W3Main','f5\\W3OH','f6\\L1448I','f7\\L1448N','f8\\L1448C','f9\\L1445','f10\\IRAS2A','f11\\SVS13','f12\\IRAS4A','f13\\IRAS4B','f14\\HH211','f15\\DGTau','f16\\L1551','f17\\L1527','f18\\CB26','f19\\OrionKL','f20\\MMS5','f20\\MMS6','f21\\FIR4','f23\\VLA1623','f24\\SerEmb17','f26\\SerEmb8','f27\\SerEmb6','f31\\B335','f32\\DR21OH','f33\\L1157', 'f34\\CB230']
    tapol_std = []
    tapol_pol = []
    hertz_std = []
    tapol_legend = []
    tapol_avg=[]
    tmp = 0    
    
    for ii in range(len(source_all)):
        try:
            tmp = 0
            tapol,scuba,hertz,sharp,Idust,xx,yy = take_data(source_all[ii])   
            
#            tapol_q = numpy.array(tapol[3])*numpy.cos(numpy.array(tapol[6])*2.0*numpy.pi/180.0)
#            tapol_u = numpy.array(tapol[3])*numpy.sin(numpy.array(tapol[6])*2.0*numpy.pi/180.0)
            
            tapol_q = numpy.cos(numpy.array(tapol[6])*2.0*numpy.pi/180.0)
            tapol_u = numpy.sin(numpy.array(tapol[6])*2.0*numpy.pi/180.0)
            tapol_avg_ang = numpy.arctan(numpy.sum(tapol_u)/numpy.sum(tapol_q))*0.5
#            tapol_pol.append(numpy.sqrt(numpy.sum(tapol_q)**2.0 + numpy.sum(tapol_u)**2.0)/numpy.sum(tapol[2]))
            tapol_pol.append(numpy.average(tapol[6]))           
            
            for i in range(len(tapol[3])):
                if (numpy.abs(tapol[6][i]*numpy.pi/180.0 - tapol_avg_ang) < numpy.pi/2.0):
                    tmp = tmp + (tapol[6][i]*numpy.pi/180.0 - tapol_avg_ang)**2.0
                else:
                    tmp = tmp + (numpy.pi - numpy.abs(tapol[6][i]*numpy.pi/180.0 - tapol_avg_ang))**2.0
            tapol_std.append(numpy.sqrt(tmp/len(tapol[3])))
            tapol_legend.append(source_all[ii])
            tapol_avg.append(tapol_avg_ang)
        except:
            print 'shit'

    return tapol[6],tapol_std,tapol_legend,tapol_avg
    

def smooth_map():

    source_all = ['f4\\W3Main','f5\\W3OH','f6\\L1448I','f7\\L1448N','f8\\L1448C','f9\\L1445','f10\\IRAS2A','f11\\SVS13','f12\\IRAS4A','f13\\IRAS4B','f14\\HH211','f15\\DGTau','f16\\L1551','f17\\L1527','f18\\CB26','f19\\OrionKL','f20\\MMS5','f20\\MMS6','f21\\FIR4','f23\\VLA1623','f24\\SerEmb17','f26\\SerEmb8','f27\\SerEmb6','f31\\B335','f32\\DR21OH','f33\\L1157', 'f34\\CB230']
    tapol_std = []
    tapol_pol = []
    hertz_std = []
    tmp = 0    
    
    for ii in range(len(source_all)):
        try:
            tmp = 0
            tapol,scuba,hertz,sharp,Idust,xx,yy = take_data(source_all[ii])
            
            beam_size = 2.94

            for i in range(len(scuba[0])):
                if (tapol[0][i]-scuba[0][i])<beam_size and (tapol[1][i]-scuba[1][i])<beam_size:
                    xtmp.append(tapol[0])
                    ytmp.append(tapol[0])
                    Ipoltmp.append()
                    Ipostmp.append()                    
                    
        except:
            print 'too bad :('

def main():
    
    source_all = ['f4\\W3Main','f5\\W3OH','f6\\L1448I','f7\\L1448N','f8\\L1448C','f9\\L1445','f10\\IRAS2A','f11\\SVS13','f12\\IRAS4A','f13\\IRAS4B','f14\\HH211','f15\\DGTau','f16\\L1551','f17\\L1527','f18\\CB26','f19\\OrionKL','f20\\MMS5','f20\\MMS6','f21\\FIR4','f23\\VLA1623','f24\\SerEmb17','f26\\SerEmb8','f27\\SerEmb6','f31\\B335','f32\\DR21OH','f33\\L1157', 'f34\\CB230']
    
    for ii in range(len(source_all)):
        try:
            tapol,scuba,hertz,sharp,Idust,xx,yy = take_data(source_all[ii])   
            Imax = max((Idust[0].data[0,0,:,:]).flatten())
            center =  numpy.where(Idust[0].data[0,0,:,:] == Imax)
            f,(ax1,ax2) = plt.subplots(1,2,figsize=(60,20))
            
            tap = range(len(tapol[0]))
            for i in range(len(tapol[0])):
                tap[i] = numpy.sqrt((tapol[0][i]-xx[center[0]])**2.0 + (tapol[1][i]-yy[center[1]])**2.0)
            ax1.scatter(tap,tapol[4],color='b',label = 'tapol')
            if scuba!=[]:
                scu = range(len(scuba[0]))
                for i in range(len(scuba[0])):
                    scu[i] = numpy.sqrt((scuba[0][i]-xx[center[0]])**2.0 + (scuba[1][i]-yy[center[1]])**2.0)
                ax1.scatter(scu,scuba[3],color='r',label='scuba')
            if hertz!=[]:
                her = range(len(hertz[0]))
                for j in range(len(hertz[0])):
                    her[j] = numpy.sqrt((hertz[0][j]-xx[center[0]])**2.0 + (hertz[1][j]-yy[center[1]])**2.0)
                ax1.scatter(her,hertz[3],color='y',label='hertz')    
        
            if sharp!=[]:
                sha = range(len(sharp[0]))
                for k in range(len(sharp[0])):
                    sha[k] = numpy.sqrt((sharp[0][k]-xx[center[0]])**2.0 + (sharp[1][k]-yy[center[1]])**2.0)
                ax1.scatter(sha,sharp[3],color='g',label='sharp')    
            ax1.legend()
            
            xx_dust,yy_dust = a.sky_coor(Idust)
            ax2.contourf(Idust[0].data[0,0,:,::-1],extent=[max(xx_dust),min(xx_dust),min(yy_dust),max(yy_dust)],origin='lower',aspect='auto')
#            qv1 = ax2.quiver(-tapol[0],tapol[1],-tapol[4]*numpy.sin(tapol[6]*numpy.pi/180.0),tapol[4]*numpy.cos(tapol[6]*numpy.pi/180.0),headwidth=0,width=0.001,scale=100,color='w',pivot='middle')    
            qv1 = ax2.quiver(-tapol[0],tapol[1],-tapol[2]*numpy.sin(tapol[6]*numpy.pi/180.0),tapol[2]*numpy.cos(tapol[6]*numpy.pi/180.0),headwidth=0,width=0.001,scale=100,color='w',pivot='middle')    

            plt.quiverkey(qv1,0.2,0.2,4,'4% Tapol')
        
            if scuba!=[]:
                qv2 = ax2.quiver(-scuba[0],scuba[1],-scuba[3]*numpy.sin(scuba[5]*numpy.pi/180.0),scuba[3]*numpy.cos(scuba[5]*numpy.pi/180.0),headwidth=0,width=0.001,color='r',scale=100,pivot='middle')    
                plt.quiverkey(qv2,0.2,0.15,4,'4% Scuba')
            if hertz!=[]:
                qv3 = ax2.quiver(-hertz[0],hertz[1],-hertz[3]*numpy.sin(hertz[5]*numpy.pi/180.0),hertz[3]*numpy.cos(hertz[5]*numpy.pi/180.0),headwidth=0,width=0.001,color='y',scale=100,pivot='middle')
                plt.quiverkey(qv3,0.2,0.1,4,'4% Hertz')
            if sharp!=[]:
                qv4 = ax2.quiver(-sharp[0],sharp[1],-sharp[3]*numpy.sin(sharp[5]*numpy.pi/180.0),sharp[3]*numpy.cos(sharp[5]*numpy.pi/180.0),headwidth=0,width=0.001,color='g',scale=100,pivot='middle')
                plt.quiverkey(qv4,0.2,0.05,4,'4% Sharp')
            
            if ii>4:
                plt.savefig(source_all[ii][4:]+'_vector.png')
                plt.clf()
            else:
                plt.savefig(source_all[ii][3:]+'_vector.png')
                plt.clf()
        except:
            print 'except',source_all[ii]


def take_data(source):
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
    scuba = []
    hertz = []
    sharp = []
    tmp1 = 'SCUBA'
    tmp2 = 'Hertz'
    
    dustdensity = fits.open(directory+source+dir_Idust)
    
    if raw!=[]:
        for i in raw:
            new[j] = map(float,i.split())
            j = j + 1
        tapol = numpy.transpose((numpy.array(new)))
    else:
        tapol = []
    if raw1!=[]:     
        for i in raw1:
            new1[k] = i.split()
            if new1[k][7] == tmp1:
                scuba.append(map(float,new1[k][:6]))
            elif new1[k][7] == tmp2:
                hertz.append(map(float,new1[k][:6]))
            else:
                sharp.append(map(float,new1[k][:6]))
        scuba = numpy.transpose(numpy.array(scuba))
        hertz = numpy.transpose(numpy.array(hertz))
        sharp = numpy.transpose(numpy.array(sharp))
    else:
        scuba=[]
        hertz=[]
        sharp=[]
     
     
    xx,yy = sky_coor(dustdensity) 
    return tapol,scuba,hertz,sharp,dustdensity,xx,yy


    

def sky_coor(col):
    xr,yr = col[0].data[0,0,:,:].shape

    xpix = col[0].header['CRPIX1']
    ypix = col[0].header['CRPIX2']
    
    xdel = col[0].header['CDELT1']
    ydel = col[0].header['CDELT2']
    
    xval = col[0].header['CRVAL1']
    yval = col[0].header['CRVAL2']   
    
    xx = (xdel*(numpy.array(range(xr)) - xpix+1)+xval)
    yy = (ydel*(numpy.array(range(yr)) - ypix+1)+yval)
    
    return xx,yy