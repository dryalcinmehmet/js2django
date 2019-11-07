#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:21:55 2019

@author: doctor
"""



import os
import re
data=''
src="/home/doctor/PycharmProjects/tubitak/battery/src/templates/dash/AdminLTE"
file_list=[]
for root, dirs, files in os.walk(src):
    for file in files:
        if file.endswith(".html"):
             file_list.append(os.path.join(root, file))           





for file in file_list:  
    
############ img ############   
#%%
    fin = open("%s"%file, "rt")
    data = fin.read()
    fin.close()
    img = re.findall('<img src="(.*jpg|.*jpeg|.*png)"', data)
    s=''
    for j in [i for i in img if not 'http' in i]:
        s =  "{0} static 'dash/{1}' {2}".format('{%',j,'%}')
        print(s)
        data = data.replace('%s'%j,s )
#        
#    fin = open("%s"%file, "wt")
#    fin.write(data)
#    fin.close()
    
    
#%%
       
############ href js css ############   
    
#%%

    fin = open("%s"%file, "rt")
    data = fin.read()
    fin.close()
    
    href = re.findall('href="(.*js|.*css)"', data)
       
    for j in [i for i in href if not 'http' in i]:
        
        if '../' in j:
            j=j.replace('../','')
        s =  "{0} static 'dash/{1}' {2}".format('{%',j,'%}')
        data = data.replace('%s'%j,s )
        s=''
        data= data.replace('../','')
        
    fin = open("%s"%file, "wt")
    fin.write(data)
    fin.close()


#%%
############ src js ############     

#%%

    fin = open("%s"%file, "rt")
    data = fin.read()
    
    fin.close()
        
   
    src = re.findall('src="(.*js|.*css)"', data)

        
    for j in [i for i in src if not 'http' in i]:
        if '../' in j:
            j=j.replace('../','')
             
        s =  "{0} static 'dash/{1}' {2}".format('{%',j,'%}')
        data = data.replace('%s'%j,s )
        s=''
        data= data.replace('../','')
        
    fin = open("%s"%file, "wt")
    fin.write(data)
    fin.close()

#%%

############ add static files ############     

#%%
    
    
    fin = open("%s"%file, "rt")
    data = fin.read()
    data='{% load staticfiles %}'+data
    
        
    fin.close()
    
    fin = open("%s"%file, "wt")
    fin.write(data)
    fin.close()
    data=''
    
#%%
##html içi url dönüşümü

import os
import re
path="/home/doctor/PycharmProjects/tubitak/battery/src/templates/dash/AdminLTE"
file_list=[]
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".html"):
             file_list.append(os.path.join(root, file))


for file in file_list:          
    fin = open("%s"%file, "rt")
    data = fin.read()
    fin.close()    
    href = re.findall('a href="(.*html)"', data)   
       
    for j in href:
        if not '-' in j:
           j_with_minus = j
                # j=href[49]
           def check_num(j):     
                try:
                    assert int(j.rsplit('/')[-1][0])
                    return True
                except:
                    return False
                
           if check_num(j)==True:
    #           print(j) 
               j_with_minus = j
               k=j.rsplit('/')[-1].replace('.html','')
    #           print(j)
               s =  "{0} url '{1}{2}' {3}".format('{%','code_',k,'%}')
               print(s)
               data = data.replace('%s'%j_with_minus,s)
               s=''  
           else:         
                s =  "{0} url '{1}' {2}".format('{%',j.rsplit('/')[-1].replace('.html',''),'%}')
                data = data.replace('%s'%j,s )
                s=''
           
           
           
           
         
        if '-' in j:
            j_with_minus = j
                 # j=href[49]
            def check_num(j):     
                try:
                    assert int(j.rsplit('/')[-1][0])
                    return True
                except:
                    return False
                
            if check_num(j)==True:
    #           print(j) 
               j_with_minus = j
               k=j.rsplit('/')[-1].replace('.html','')
    #           print(j)
               s =  "{0} url '{1}{2}' {3}".format('{%','code_',k,'%}')
               print(s)
               data = data.replace('%s'%j_with_minus,s)
               s=''  
            else:   
                j=j.rsplit('/')[-1].replace('-','')
                s =  "{0} url '{1}' {2}".format('{%',j.rsplit('/')[-1].replace('.html',''),'%}')
                data = data.replace('%s'%j_with_minus,s )
                s=''
           
       
      
    fin = open("%s"%file, "wt")
    fin.write(data)
    fin.close()
  
#### url and view ####

#%%        
import os,re
path="/home/doctor/PycharmProjects/tubitak/battery/src/templates/dash/AdminLTE"
file_list=[]
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".html"):
             file_list.append(os.path.join(root, file))

urls="/home/doctor/PycharmProjects/tubitak/battery/src/battery/urls.py"
views="/home/doctor/PycharmProjects/tubitak/battery/src/battery/views.py"
url_patterns=[]
 
class_views = []
  
      
for j in file_list:
    


    def check_num(j):     
        try:
            assert int(j.rsplit('/')[-1][0])
            return True
        except:
            return False
        
    if check_num(j)==True:
#           print(j) 
       j_with_minus = j
       k=j.rsplit('/')[-1].replace('.html','')
#           print(j)
       
       url_path=  '''path("code_{0}", views.code_{1}Page.as_view(), name="code_{2}"),'''.format(j.rsplit('/')[-1].replace('.html',''),
                     j.rsplit('/')[-1].replace('.html','').replace('-',''),j.rsplit('/')[-1].replace('.html','').replace('-',''))
       url_patterns.append(url_path)
        
       class_str = '''class code_{0}Page(generic.TemplateView):\n \t template_name = "{1}"\n \n \n'''.format(j.rsplit('/')[-1].replace('.html',''),j.replace(os.getcwd(),'')[0:])
       class_views.append(class_str)

       
   
    else:
        url_path=  '''path("{0}/", views.{1}Page.as_view(), name="{2}"),'''.format(j.rsplit('/')[-1].replace('.html','').replace('-',''),
                     j.rsplit('/')[-1].replace('.html','').replace('-',''),j.rsplit('/')[-1].replace('.html','').replace('-',''))
        url_patterns.append(url_path)
        
        class_str = '''class {0}Page(generic.TemplateView):\n \t template_name = "{1}"\n \n \n'''.format(j.rsplit('/')[-1].replace('.html','').replace('-',''),j.replace(os.getcwd(),'')[1:])
        class_views.append(class_str)
    
    
fin = open("%s"%urls, "rt")
data = fin.read()
fin.close() 
data= data.split("\n")
for j in [i.replace(' ','') for i in data if ('urlpatterns +=' not in i) and ('path(' in i)]:
        url_patterns.append(j)


   
    
fin = open("%s"%urls, "at")
fin.write('urlpatterns= {} /n'.format([' '.join(word for word in url_patterns)]).replace("'",''))
fin.close()

for i in class_views:    
    fin = open("%s"%views, "at")
    fin.write(i)
    fin.close()
 





