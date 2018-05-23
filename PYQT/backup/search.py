# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from urllib2 import urlopen
import json
import codecs
import re
from random import *
import os
from collections import Counter

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_label_platform(object):
    def call_me(self):
        print("----------------------------------------------------------------------------------------------------")
        self.listWidget.clear()
        self.titles_final =   []
        self.genres_final =    []
        self.platforms_final = []
        self.ratings_final =   []
        self.releases_final =  []
        self.title_input = self.lineEdit_title.text()
        self.genre_input = self.comboBox_3.currentText()
        self.platform_input = self.comboBox_2.currentText()
        self.rating_input = self.comboBox.currentText()
        self.ch_rel = False
        self.ch_top = False
        self.ch_rec = False
        self.ch_exc = False
        self.ch_sug = False
        self.ch_rel = self.checkBox_related.isChecked()
        self.ch_top = self.checkBox_top_rated.isChecked()
        self.ch_rec = self.checkBox_recent.isChecked()
        self.ch_exc = self.checkBox_exact.isChecked()
        self.ch_sug = self.checkBox_suggest.isChecked()
        if(self.genre_input!=""):
            f=open("genre.txt", "a+")
            f.write(self.genre_input + "\n")
        if(self.platform_input!=""):
            f=open("platform.txt", "a+")
            f.write(self.platform_input + "\n")
        ###very basic search
        if(self.ch_rel == False and self.ch_top == False and self.ch_rec == False and self.ch_exc == False and self.ch_sug == False):
            #print("inside very basic search")
            self.titles_final, self.genres_final, self.platforms_final, self.ratings_final, self.releases_final = self.very_basic_search(self.title_input, self.genre_input, self.platform_input, self.rating_input, 0)
            #self.stdout_print(self.listWidget, self.titles_final, self.genres_final, self.platforms_final, self.ratings_final, self.releases_final) #stdout 1
            self.listWidget.clear()
            for x in range(0, len(self.titles_final)):
                self.listWidget.addItem("Title: "+self.titles_final[x])
                self.listWidget.addItem("Genre: "+ self.genres_final[x])
                self.listWidget.addItem("Platform: "+ self.platforms_final[x])
                self.tmp = ""
                if(self.ratings_final[x]=="3"):
                    self.tmp = "Rating: " + "Very Low"
                elif(self.ratings_final[x]=="7"):
                    self.tmp = "Rating: " + "Low"
                elif(self.ratings_final[x]=="12"):
                    self.tmp = "Rating: " + "Medium"
                elif(self.ratings_final[x]=="16"):
                    self.tmp = "Rating: " + "High"
                elif(self.ratings_final[x]=="18"):
                    self.tmp = "Rating: " + "Very High"
                else:
                    self.tmp = "Not Rated"
                self.listWidget.addItem(self.tmp)
                self.listWidget.addItem("Release: "+ self.releases_final[x])
                self.listWidget.addItem("\n")
        ###suggest
        elif(self.ch_sug == True):
            #print("inside suggest")
            f = open('genre.txt', 'r')
            self.genre_cache = f.readlines()
            f.close()
            f = open('platform.txt', 'r')
            self.platform_cache = f.readlines()
            f.close()
            if(len(self.genre_cache)==0 and len(self.platform_cache)==0):
                self.ch_rel = False
                self.ch_top = False
                self.ch_rec = False
                self.ch_exc = False
                self.ch_sug = False
                self.titles_final.append("No suggestion found!");
                self.genres_final.append("No suggestion found!");
                self.platforms_final.append("No suggestion found!");
                self.ratings_final.append("No suggestion found!");
                self.releases_final.append("No suggestion found!");
                #self.stdout_print(self.listWidget, self.titles_final, self.genres_final, self.platforms_final, self.ratings_final, self.releases_final) #stdout 2
                self.listWidget.clear()
                for x in range(0, len(self.titles_final)):
                    self.listWidget.addItem("Title: "+self.titles_final[x])
                    self.listWidget.addItem("Genre: "+ self.genres_final[x])
                    self.listWidget.addItem("Platform: "+ self.platforms_final[x])
                    self.tmp = ""
                    if(self.ratings_final[x]=="3"):
                        self.tmp = "Rating: " + "Very Low"
                    elif(self.ratings_final[x]=="7"):
                        self.tmp = "Rating: " + "Low"
                    elif(self.ratings_final[x]=="12"):
                        self.tmp = "Rating: " + "Medium"
                    elif(self.ratings_final[x]=="16"):
                        self.tmp = "Rating: " + "High"
                    elif(self.ratings_final[x]=="18"):
                        self.tmp = "Rating: " + "Very High"
                    else:
                        self.tmp = "Rating: No suggestion found!"
                    self.listWidget.addItem(self.tmp)
                    self.listWidget.addItem("Release: "+ self.releases_final[x])
                    self.listWidget.addItem("\n")			
            else:
                self.genre_sug = ""
                self.platform_sug = ""
                if(len(self.genre_cache)!=0):
                    self.genre_sug_dict = Counter(self.genre_cache)
                    self.genre_sug_pull = self.genre_sug_dict.most_common()[0][0]
                    self.genre_sug = self.genre_sug_pull.replace("\n", "")
                if(len(self.platform_cache)!=0):
                    self.platform_sug_dict = Counter(self.platform_cache)
                    self.platform_sug_pull = self.platform_sug_dict.most_common()[0][0]
                    self.platform_sug = self.platform_sug_pull.replace("\n", "")
                self.titles_final, self.genres_final, self.platforms_final, self.ratings_final, self.releases_final = self.very_basic_search("", self.genre_sug, self.platform_sug, "Very High", 0)
                self.ch_rel = False
                self.ch_top = False
                self.ch_rec = False
                self.ch_exc = False
                self.ch_sug = False
                self.rando = 0
                if(len(self.titles_final)!=0):
                    self.rando = randint(0, len(self.titles_final)-1) 
                else:
                    self.rando = 0
                self.tit_final = []
                self.gen_final = []
                self.plat_final = []
                self.rat_final = []
                self.rel_final = []
                self.tit_final.append(self.titles_final[self.rando])
                self.gen_final.append(self.genres_final[self.rando])
                self.plat_final.append(self.platforms_final[self.rando])
                self.rat_final.append(self.ratings_final[self.rando])
                self.rel_final.append(self.releases_final[self.rando])
                #self.stdout_print(self.listWidget, self.tit_final, self.gen_final, self.plat_final, self.rat_final, self.rel_final) #stdout 3
                self.listWidget.clear()
                for x in range(0, len(self.tit_final)):
                    self.listWidget.addItem("Tile: "+self.tit_final[x])
                    self.listWidget.addItem("Genre: "+ self.gen_final[x])
                    self.listWidget.addItem("Platform: "+ self.plat_final[x])
                    self.tmp = ""
                    if(self.rat_final[x]=="3"):
                        self.tmp = "Rating: " + "Very Low"
                    elif(self.rat_final[x]=="7"):
                        self.tmp = "Rating: " + "Low"
                    elif(self.rat_final[x]=="12"):
                        self.tmp = "Rating: " + "Medium"
                    elif(self.rat_final[x]=="16"):
                        self.tmp = "Rating: " + "High"
                    elif(self.rat_final[x]=="18"):
                        self.tmp = "Rating: " + "Very High"
                    else:
                        self.tmp = "Rating: No suggestion found!"
                    self.listWidget.addItem(self.tmp)
                    self.listWidget.addItem("Release: "+ self.rel_final[x])
                    self.listWidget.addItem("\n")
        ###exact match
        elif(self.ch_exc==True):
            #print("inside exact match")
            if(self.title_input!=""):
                self.titles_final, self.genres_final, self.platforms_final, self.ratings_final, self.releases_final = self.very_basic_search(self.title_input, self.genre_input, self.platform_input, self.rating_input, 0)	 
            self.exact_index = -1
            self.exact_tlte = ""
            self.exact_genre = ""
            self.exact_platform = ""
            self.exact_rating = ""
            self.exact_release = ""
            self.title_input = self.title_input.replace("%20", " ")
            if(len(self.titles_final)!=0):
                for x in range (0, len(self.titles_final)):
                    if(str(self.titles_final[x]).lower()==str(self.title_input).lower()):
                        self.exact_index = x
                if(self.exact_index!=-1):
                    self.exact_title = self.titles_final[self.exact_index]
                    self.exact_genre = self.genres_final[self.exact_index]
                    self.exact_platform = self.platforms_final[self.exact_index]
                    self.exact_rating = self.ratings_final[self.exact_index]
                    self.exact_release = self.releases_final[self.exact_index]
                    self.ch_top = False
                    self.ch_sug = False
                    self.ch_exc = False
                    self.ch_rel = False
                    self.ch_rec = False
                    self.listWidget.clear() #stdout 3.1
                    self.listWidget.addItem("Title: "+ self.exact_title)
                    self.listWidget.addItem("Genre: "+ self.exact_genre)
                    self.listWidget.addItem("Platform: "+ self.exact_platform)
                    if(self.exact_rating=="3"):
                        self.listWidget.addItem("Rating: Very Low")
                    if(self.exact_rating=="7"):
                        self.listWidget.addItem("Rating: Low")
                    if(self.exact_rating=="12"):
                        self.listWidget.addItem("Rating: Medium")
                    if(self.exact_rating=="16"):
                        self.listWidget.addItem("Rating: High")
                    if(self.exact_rating=="18"):
                        self.listWidget.addItem("Rating: Very High")
                    self.listWidget.addItem("Release: "+ self.exact_release)
                else:
                    self.exact_title = []
                    self.exact_title.append("No exact match")
                    self.exact_genre = []
                    self.exact_genre.append("No exact match")
                    self.exact_platform = []
                    self.exact_platform.append("No exact match")
                    self.exact_rating = []
                    self.exact_rating.append("No exact match")
                    self.exact_release = []
                    self.exact_release.append("No exact match")
                    self.ch_top = False
                    self.ch_sug = False
                    self.ch_exc = False
                    self.ch_rel = False
                    self.ch_rec = False
                    #self.stdout_print(self.listWidget, self.exact_title, self.exact_genre, self.exact_platform, self.exact_rating, self.exact_release) #stdout 4
                    self.listWidget.clear()
                    for x in range(0, len(self.exact_title)):
                        self.listWidget.addItem("Tile: "+self.exact_title[x])
                        self.listWidget.addItem("Genre: "+ self.exact_genre[x])
                        self.listWidget.addItem("Platform: "+ self.exact_platform[x])
                        self.tmp = ""
                        if(self.exact_rating[x]=="3"):
                            self.tmp = "Rating: " + "Very Low"
                        elif(self.exact_rating[x]=="7"):
                            self.tmp = "Rating: " + "Low"
                        elif(self.exact_rating[x]=="12"):
                            self.tmp = "Rating: " + "Medium"
                        elif(self.exact_rating[x]=="16"):
                            self.tmp = "Rating: " + "High"
                        elif(self.exact_rating[x]=="18"):
                            self.tmp = "Rating: " + "Very High"
                        else:
                            self.tmp = "No exact match"
                        self.listWidget.addItem(self.tmp)
                        self.listWidget.addItem("Release: "+ self.exact_release[x])
                        self.listWidget.addItem("\n")
            else:
                self.exact_title = []
                self.exact_title.append("No exact match")
                self.exact_genre = []
                self.exact_genre.append("No exact match")
                self.exact_platform = []
                self.exact_platform.append("No exact match")
                self.exact_rating = []
                self.exact_rating.append("No exact match")
                self.exact_release = []
                self.exact_release.append("No exact match")
                self.ch_top = False
                self.ch_sug = False
                self.ch_exc = False
                self.ch_rel = False
                self.ch_rec = False
                #self.stdout_print(self.listWidget, self.exact_title, self.exact_genre, self.exact_platform, self.exact_rating, self.exact_release) #stdout 5
                self.listWidget.clear()
                for x in range(0, len(self.exact_title)):
                    self.listWidget.addItem("Tile: "+self.exact_title[x])
                    self.listWidget.addItem("Genre: "+ self.exact_genre[x])
                    self.listWidget.addItem("Platform: "+ self.exact_platform[x])
                    self.tmp = ""
                    if(self.exact_rating[x]=="3"):
                        self.tmp = "Rating: " + "Very Low"
                    elif(self.exact_rating[x]=="7"):
                        self.tmp = "Rating: " + "Low"
                    elif(self.exact_rating[x]=="12"):
                        self.tmp = "Rating: " + "Medium"
                    elif(self.exact_rating[x]=="16"):
                        self.tmp = "Rating: " + "High"
                    elif(self.exact_rating[x]=="18"):
                        self.tmp = "Rating: " + "Very High"
                    else:
                        self.tmp = "No Exact match"
                    self.listWidget.addItem(self.tmp)
                    self.listWidget.addItem("Release: "+ self.exact_release[x])
                    self.listWidget.addItem("\n")
        ###show related
        elif(self.ch_rel == True):
            #print("inside show related")
            if(self.ch_top== True):
                self.titles_final, self.genres_final, self.platforms_final, self.ratings_final, self.releases_final = self.very_basic_search("", self.genre_input, "", "Very High", 0)
            else:
                self.titles_final, self.genres_final, self.platforms_final, self.ratings_final, self.releases_final = self.very_basic_search(self.title_input, self.genre_input, "", self.rating_input, 0)
            if(self.ch_rec==True):
                self.title_rec = []
                self.genre_rec = []
                self.platform_rec = []
                self.rating_rec = []
                self.release_rec = []
                self.recent_index = []
                for x in range(0, len(self.releases_final)):
                    if(self.releases_final[x]=="2017"):
                        self.recent_index.append(x)
                for x in range(0, len(self.releases_final)):
                    if(self.releases_final[x]=="2016"):
                        self.recent_index.append(x)
                for x in range(0, len(self.releases_final)):
                    if(self.releases_final[x]=="2015"):
                        self.recent_index.append(x)
                for x in range(0, len(self.releases_final)):
                    if(self.releases_final[x]=="2014"):
                        self.recent_index.append(x)
                for x in range(0, len(self.releases_final)):
                    if(self.releases_final[x]=="2013"):
                        self.recent_index.append(x)
                for x in range(0, len(self.releases_final)):
                    if(self.releases_final[x]=="2012"):
                        self.recent_index.append(x)
                for x in range(0, len(self.recent_index)):
                    self.title_rec.append(self.titles_final[self.recent_index[x]])
                    self.genre_rec.append(self.genres_final[self.recent_index[x]])
                    self.platform_rec.append(self.platforms_final[self.recent_index[x]])
                    self.rating_rec.append(self.ratings_final[self.recent_index[x]])
                    self.release_rec.append(self.releases_final[self.recent_index[x]])
                self.ch_exc = False
                self.ch_rec = False
                self.ch_rel = False
                self.ch_sug = False
                self.ch_top = False
                #self.stdout_print(self.listWidget, self.title_rec, self.genre_rec, self.platform_rec, self.rating_rec, self.release_rec) #stdout 6
                self.listWidget.clear()
                for x in range(0, len(self.title_rec)):
                    self.listWidget.addItem("Title: "+self.title_rec[x])
                    self.listWidget.addItem("Genre: "+ self.genre_rec[x])
                    self.listWidget.addItem("Platform: "+ self.platform_rec[x])
                    self.tmp = ""
                    if(self.rating_rec[x]=="3"):
                        self.tmp = "Rating: " + "Very Low"
                    elif(self.rating_rec[x]=="7"):
                        self.tmp = "Rating: " + "Low"
                    elif(self.rating_rec[x]=="12"):
                        self.tmp = "Rating: " + "Medium"
                    elif(self.rating_rec[x]=="16"):
                        self.tmp = "Rating: " + "High"
                    elif(self.rating_rec[x]=="18"):
                        self.tmp = "Rating: " + "Very High"
                    else:
                        self.tmp = "No Exact match"
                    self.listWidget.addItem(self.tmp)
                    self.listWidget.addItem("Release: "+ self.release_rec[x])
                    self.listWidget.addItem("\n")
            else: 
                self.ch_top = False
                self.ch_sug = False
                self.ch_rel = False
                self.ch_rec = False
                self.ch_exc = False
                #self.stdout_print(self.listWidget, self.titles_final, self.genres_final, self.platforms_final, self.ratings_final, self.releases_final) #stdout 7
                self.listWidget.clear()
                for x in range(0, len(self.titles_final)):
                    self.listWidget.addItem("Title: "+self.titles_final[x])
                    self.listWidget.addItem("Genre: "+ self.genres_final[x])
                    self.listWidget.addItem("Platform: "+ self.platforms_final[x])
                    self.tmp = ""
                    if(self.ratings_final[x]=="3"):
                        self.tmp = "Rating: " + "Very Low"
                    elif(self.ratings_final[x]=="7"):
                        self.tmp = "Rating: " + "Low"
                    elif(self.ratings_final[x]=="12"):
                        self.tmp = "Rating: " + "Medium"
                    elif(self.ratings_final[x]=="16"):
                        self.tmp = "Rating: " + "High"
                    elif(self.ratings_final[x]=="18"):
                        self.tmp = "Rating: " + "Very High"
                    else:
                        self.tmp = "No Exact match"
                    self.listWidget.addItem(self.tmp)
                    self.listWidget.addItem("Release: "+ self.releases_final[x])
                    self.listWidget.addItem("\n")
					
        ###high rating
        elif(self.ch_top== True):
            #print("inside high rating")
            self.titles_final, self.genres_final, self.platforms_final, self.ratings_final, self.releases_final = self.very_basic_search("", self.genre_input, self.platform_input, "Very High", 0)
            if(self.ch_rec== True):
                self.title_rec = []
                self.genre_rec = []
                self.platform_rec = []
                self.rating_rec = []
                self.release_rec = []
                self.recent_index = []
                for x in range(0, len(self.releases_final)):
                    if(self.releases_final[x]=="2017"):
                        self.recent_index.append(x)
                for x in range(0, len(self.releases_final)):
                    if(self.releases_final[x]=="2016"):
                        self.recent_index.append(x)
                for x in range(0, len(self.releases_final)):
                    if(self.releases_final[x]=="2015"):
                        self.recent_index.append(x)
                for x in range(0, len(self.releases_final)):
                    if(self.releases_final[x]=="2014"):
                        self.recent_index.append(x)
                for x in range(0, len(self.releases_final)):
                    if(self.releases_final[x]=="2013"):
                        self.recent_index.append(x)
                for x in range(0, len(self.releases_final)):
                    if(self.releases_final[x]=="2012"):
                        self.recent_index.append(x)
                for x in range(0, len(self.recent_index)):
                    self.title_rec.append(self.titles_final[self.recent_index[x]])
                    self.genre_rec.append(self.genres_final[self.recent_index[x]])
                    self.platform_rec.append(self.platforms_final[self.recent_index[x]])
                    self.rating_rec.append(self.ratings_final[self.recent_index[x]])
                    self.release_rec.append(self.releases_final[self.recent_index[x]])
                self.ch_exc = False
                self.ch_rec = False
                self.ch_rel = False
                self.ch_sug = False
                self.ch_top = False
                #self.stdout_print(self.listWidget, self.title_rec, self.genre_rec, self.platform_rec, self.rating_rec, self.release_rec) #stdout 8
                self.listWidget.clear()
                for x in range(0, len(self.title_rec)):
                    self.listWidget.addItem("Title: "+self.title_rec[x])
                    self.listWidget.addItem("Genre: "+ self.genre_rec[x])
                    self.listWidget.addItem("Platform: "+ self.platform_rec[x])
                    self.tmp = ""
                    if(self.rating_rec[x]=="3"):
                        self.tmp = "Rating: " + "Very Low"
                    elif(self.rating_rec[x]=="7"):
                        self.tmp = "Rating: " + "Low"
                    elif(self.rating_rec[x]=="12"):
                        self.tmp = "Rating: " + "Medium"
                    elif(self.rating_rec[x]=="16"):
                        self.tmp = "Rating: " + "High"
                    elif(self.rating_rec[x]=="18"):
                        self.tmp = "Rating: " + "Very High"
                    else:
                        self.tmp = "No Exact match"
                    self.listWidget.addItem(self.tmp)
                    self.listWidget.addItem("Release: "+ self.release_rec[x])
                    self.listWidget.addItem("\n")
            else:
                self.ch_exc = False
                self.ch_rec = False
                self.ch_rel = False
                self.ch_sug = False
                self.ch_top = False
                #self.stdout_print(self.listWidget, self.titles_final, self.genres_final, self.platforms_final, self.ratings_final, self.releases_final) #stdout 9
                self.listWidget.clear()
                for x in range(0, len(self.titles_final)):
                    self.listWidget.addItem("Tile: "+self.titles_final[x])
                    self.listWidget.addItem("Genre: "+ self.genres_final[x])
                    self.listWidget.addItem("Platform: "+ self.platforms_final[x])
                    self.tmp = ""
                    if(self.ratings_final[x]=="3"):
                        self.tmp = "Rating: " + "Very Low"
                    elif(self.ratings_final[x]=="7"):
                        self.tmp = "Rating: " + "Low"
                    elif(self.ratings_final[x]=="12"):
                        self.tmp = "Rating: " + "Medium"
                    elif(self.ratings_final[x]=="16"):
                        self.tmp = "Rating: " + "High"
                    elif(self.ratings_final[x]=="18"):
                        self.tmp = "Rating: " + "Very High"
                    else:
                        self.tmp = "No Exact match"
                    self.listWidget.addItem(self.tmp)
                    self.listWidget.addItem("Release: "+ self.releases_final[x])
                    self.listWidget.addItem("\n")
        ###newest to oldest
        elif(self.ch_rec == True):
            #print("inside newest ones")
            self.titles_final, self.genres_final, self.platforms_final, self.ratings_final, self.releases_final = self.very_basic_search("", self.genre_input, self.platform_input,self.rating_input, 0)
            self.title_rec = []
            self.genre_rec = []
            self.platform_rec = []
            self.rating_rec = []
            self.release_rec = []
            self.recent_index = []
            for x in range(0, len(self.releases_final)):
                if(self.releases_final[x]=="2017"):
                    self.recent_index.append(x)
            for x in range(0, len(self.releases_final)):
                if(self.releases_final[x]=="2016"):
                    self.recent_index.append(x)
            for x in range(0, len(self.releases_final)):
                if(self.releases_final[x]=="2015"):
                    self.recent_index.append(x)
            for x in range(0, len(self.releases_final)):
                if(self.releases_final[x]=="2014"):
                    self.recent_index.append(x)
            for x in range(0, len(self.releases_final)):
                if(self.releases_final[x]=="2013"):
                    self.recent_index.append(x)
            for x in range(0, len(self.releases_final)):
                if(self.releases_final[x]=="2012"):
                    self.recent_index.append(x)
            for x in range(0, len(self.recent_index)):
                self.title_rec.append(self.titles_final[self.recent_index[x]])
                self.genre_rec.append(self.genres_final[self.recent_index[x]])
                self.platform_rec.append(self.platforms_final[self.recent_index[x]])
                self.rating_rec.append(self.ratings_final[self.recent_index[x]])
                self.release_rec.append(self.releases_final[self.recent_index[x]])
            self.ch_exc = False
            self.ch_rec = False
            self.ch_rel = False
            self.ch_sug = False
            self.ch_top = False
            #self.stdout_print(self.listWidget, self.title_rec, self.genre_rec, self.platform_rec, self.rating_rec, self.release_rec) #stdout 10
            self.listWidget.clear()
            for x in range(0, len(self.title_rec)):
                self.listWidget.addItem("Title: "+self.title_rec[x])
                self.listWidget.addItem("Genre: "+ self.genre_rec[x])
                self.listWidget.addItem("Platform: "+ self.platform_rec[x])
                self.tmp = ""
                if(self.rating_rec[x]=="3"):
                    self.tmp = "Rating: " + "Very Low"
                elif(self.rating_rec[x]=="7"):
                    self.tmp = "Rating: " + "Low"
                elif(self.rating_rec[x]=="12"):
                    self.tmp = "Rating: " + "Medium"
                elif(self.rating_rec[x]=="16"):
                    self.tmp = "Rating: " + "High"
                elif(self.rating_rec[x]=="18"):
                    self.tmp = "Rating: " + "Very High"
                else:
                    self.tmp = "No Exact match"
                self.listWidget.addItem(self.tmp)
                self.listWidget.addItem("Release: "+ self.release_rec[x])
                self.listWidget.addItem("\n")
					
					
    def stdout_print(self, listWidgettt, title_result, genre_result, platform_result, rating_result, release_result):
        self.output = ""
        self.listWidget.clear()
        for x in range(0, len(title_result)):
            #self.output = self.output + "Title: " + title_result[x] + "\n"
            self.listWidget.addItem("Title: " + title_result[x])
            #self.output = self.output + "Genre: " + genre_result[x] + "\n"
            self.listWidget.addItem("Genre: " + genre_result[x])
            #self.output = self.output + "Platform: " + platform_result[x] + "\n"
            self.listWidget.addItem("Platform: " + platform_result[x])
            if(rating_result[x]=="3"):
                self.output = "Rating: " + "Very Low"
            elif(rating_result[x]=="7"):
                self.output ="Rating: " + "Low"
            elif(rating_result[x]=="12"):
                self.output ="Rating: " + "Medium"
            elif(rating_result[x]=="16"):
                self.output ="Rating: " + "High"
            elif(rating_result[x]=="18"):
                self.output ="Rating: " + "Very High"
            self.listWidget.addItem("Rating: "+ rating_result[x])
            #self.output = self.output + "Release: " + release_result[x] + "\n"
            self.listWidget.addItem("Release: " + release_result[x])
            self.listWidget.addItem("\n")
            #self.output = self.output + "\n"
        #print(self.output)
        #self.listWidget.clear()
        #listWidget.addItem(self.output)
		
		
    #indicator 0 = very basic
    #1 = suggest(very basic wo title)
    #2 = exact(very basic with all)
    #3 = related(very basic w genre only)
    #4 = high rating(very basic w genre+plaform)
    #5 = very basic with genre+platform
    def very_basic_search(self, title_input, genre_input, platform_input, rating_input, indicator):
        self.titles_parsed = []
        self.genres_parsed = []
        self.platform_parsed = []
        self.rating_parsed = []
        self.release_parsed = []
        rating = 0
        if(rating_input=="Very High"):
            rating = "18"
        elif(rating_input=="High"):
           rating = "16"
        elif(rating_input=="Medium"):
            rating = "12"
        elif(rating_input=="Very Low"):
            rating = "7"
        elif(rating_input=="Low"):
            rating = "3"
        else:
            rating = "0"
        if(indicator == 0):
            switch = 0	
            url = ""
            base_url = "http://192.168.56.1:8983/solr/task3/select?"
            title_url=""
            genre_url = ""
            platform_url = ""
            if(title_input!=""):
                temp = title_input.replace(" ", "%20")
                title_url = "q=title:" + temp
                if(switch==0):
                    url = base_url + title_url
                    switch = 1
            if(genre_input!=""):
                genre_url = "q=genre:"+ genre_input
                if(switch==0):
                    url= base_url+genre_url
                    switch = 1
                else:
                    url = url + "&f"+ genre_url
            if(platform_input!=""):
                platform_url = "q=platform:"+ platform_input
                if(switch==0):
                    url = base_url+platform_url
                    switch = 1
                else:
                    url = url + "&f" + platform_url
            url = url + "&rows=25000"
            print(url)
            self.response = urlopen(str(url))
            self.str_response = self.response.read().decode('utf-8')
            self.obj = json.loads(self.str_response)
            self.num_of_jsons = self.obj["response"]["numFound"]
            #print("basic search found: "+ str(self.num_of_jsons))
            #if(self.num_of_jsons>100):
            #    self.num_of_jsons = 100
            #else:
            #    self.num_of_jsons = self.num_of_jsons
            for x in range(0, self.num_of_jsons):
                self.titles_parsed.append(self.obj["response"]["docs"][x]["title"][0].encode('utf-8'))
                self.genres_parsed.append(self.obj["response"]["docs"][x]["genre"][0].encode('utf-8'))
                self.platform_parsed.append(self.obj["response"]["docs"][x]["platform"][0].encode('utf-8'))		
                if("rating" not in self.obj["response"]["docs"][x]):
                    self.rating_parsed.append("3")
                else:
                    self.rating_parsed.append(str(self.obj["response"]["docs"][x]["rating"][0]))	
                if("release" not in self.obj["response"]["docs"][x]):
                    self.release_parsed.append("1999")		
                else:				
                    temp_rel = str(self.obj["response"]["docs"][x]["release"][0][0]) + str(self.obj["response"]["docs"][x]["release"][0][1]) + str(self.obj["response"]["docs"][x]["release"][0][2]) + str(self.obj["response"]["docs"][x]["release"][0][3])
                    self.release_parsed.append(temp_rel)
            if(rating!="0"):
                self.temp_rating_index = []
                for x in range (0, len(self.rating_parsed)):
                    if(self.rating_parsed[x]==rating):
                        self.temp_rating_index.append(x)
                self.temp_titles_parsed = []
                self.temp_genres_parsed = []
                self.temp_platform_parsed = []
                self.temp_rating_parsed = []
                self.temp_release_parsed = []
                for x in range (0, len(self.temp_rating_index)):
                    self.temp_titles_parsed.append(self.titles_parsed[self.temp_rating_index[x]])
                    self.temp_genres_parsed.append(self.genres_parsed[self.temp_rating_index[x]])
                    self.temp_platform_parsed.append(self.platform_parsed[self.temp_rating_index[x]])
                    self.temp_rating_parsed.append(self.rating_parsed[self.temp_rating_index[x]])
                    self.temp_release_parsed.append(self.release_parsed[self.temp_rating_index[x]])
                return self.temp_titles_parsed, self.temp_genres_parsed, self.temp_platform_parsed, self.temp_rating_parsed, self.temp_release_parsed
            else:        
                return self.titles_parsed, self.genres_parsed, self.platform_parsed, self.rating_parsed, self.release_parsed
		
    def setupUi(self, label_platform):
        label_platform.setObjectName(_fromUtf8("label_platform"))
        label_platform.resize(1060, 641)
        label_platform.setStyleSheet(_fromUtf8("background-image: url(:/newPrefix/kratos-and-atreus-4k-kn-1280x720_111.jpg);"))
        self.pushButton_Search = QtGui.QPushButton(label_platform)
        self.pushButton_Search.setGeometry(QtCore.QRect(160, 500, 112, 34))
        self.pushButton_Search.setObjectName(_fromUtf8("pushButton_Search"))
        self.pushButton_Search.clicked.connect(self.call_me)
        self.lineEdit_title = QtGui.QLineEdit(label_platform)
        self.lineEdit_title.setGeometry(QtCore.QRect(160, 40, 171, 27))
        self.lineEdit_title.setObjectName(_fromUtf8("lineEdit_title"))
        self.label_title = QtGui.QLabel(label_platform)
        self.label_title.setGeometry(QtCore.QRect(70, 40, 70, 21))
        self.label_title.setObjectName(_fromUtf8("label_title"))
        self.label_genre = QtGui.QLabel(label_platform)
        self.label_genre.setGeometry(QtCore.QRect(70, 90, 70, 21))
        self.label_genre.setObjectName(_fromUtf8("label_genre"))
        self.label_platform_2 = QtGui.QLabel(label_platform)
        self.label_platform_2.setGeometry(QtCore.QRect(70, 140, 70, 21))
        self.label_platform_2.setObjectName(_fromUtf8("label_platform_2"))
        self.label_rating = QtGui.QLabel(label_platform)
        self.label_rating.setGeometry(QtCore.QRect(70, 190, 70, 21))
        self.label_rating.setObjectName(_fromUtf8("label_rating"))
        self.checkBox_related = QtGui.QCheckBox(label_platform)
        self.checkBox_related.setGeometry(QtCore.QRect(70, 260, 131, 25))
        self.checkBox_related.setObjectName(_fromUtf8("checkBox_related"))
        self.checkBox_top_rated = QtGui.QCheckBox(label_platform)
        self.checkBox_top_rated.setGeometry(QtCore.QRect(70, 300, 151, 25))
        self.checkBox_top_rated.setObjectName(_fromUtf8("checkBox_top_rated"))
        self.checkBox_recent = QtGui.QCheckBox(label_platform)
        self.checkBox_recent.setGeometry(QtCore.QRect(70, 340, 131, 25))
        self.checkBox_recent.setObjectName(_fromUtf8("checkBox_recent"))
        self.checkBox_exact = QtGui.QCheckBox(label_platform)
        self.checkBox_exact.setGeometry(QtCore.QRect(70, 380, 181, 25))
        self.checkBox_exact.setObjectName(_fromUtf8("checkBox_exact"))
        self.checkBox_suggest = QtGui.QCheckBox(label_platform)
        self.checkBox_suggest.setGeometry(QtCore.QRect(70, 420, 161, 25))
        self.checkBox_suggest.setObjectName(_fromUtf8("checkBox_suggest"))
        self.comboBox = QtGui.QComboBox(label_platform)
        self.comboBox.setGeometry(QtCore.QRect(160, 190, 171, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(0, _fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox_2 = QtGui.QComboBox(label_platform)
        self.comboBox_2.setGeometry(QtCore.QRect(160, 140, 171, 27))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.setItemText(0, _fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_3 = QtGui.QComboBox(label_platform)
        self.comboBox_3.setGeometry(QtCore.QRect(160, 90, 171, 27))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.setItemText(0, _fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.listWidget = QtGui.QListWidget(label_platform)
        self.listWidget.setGeometry(QtCore.QRect(740, 10, 311, 611))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.listWidget.setLineWidth(1)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))

        self.retranslateUi(label_platform)
        QtCore.QMetaObject.connectSlotsByName(label_platform)

    def retranslateUi(self, label_platform):
        label_platform.setWindowTitle(_translate("label_platform", "Dialog", None))
        self.pushButton_Search.setText(_translate("label_platform", "Search", None))
        self.label_title.setText(_translate("label_platform", "Title: ", None))
        self.label_genre.setText(_translate("label_platform", "Genre: ", None))
        self.label_platform_2.setText(_translate("label_platform", "Platform: ", None))
        self.label_rating.setText(_translate("label_platform", "Rating: ", None))
        self.checkBox_related.setText(_translate("label_platform", "Show Related", None))
        self.checkBox_top_rated.setText(_translate("label_platform", "Show Top Rated", None))
        self.checkBox_recent.setText(_translate("label_platform", "Show New", None))
        self.checkBox_exact.setText(_translate("label_platform", "Show Exact Search", None))
        self.checkBox_suggest.setText(_translate("label_platform", "Suggest Me One", None))
        self.comboBox.setItemText(1, _translate("label_platform", "Very Low", None))
        self.comboBox.setItemText(2, _translate("label_platform", "Low", None))
        self.comboBox.setItemText(3, _translate("label_platform", "Medium", None))
        self.comboBox.setItemText(4, _translate("label_platform", "High", None))
        self.comboBox.setItemText(5, _translate("label_platform", "Very High", None))
        self.comboBox_2.setItemText(1, _translate("label_platform", "PC", None))
        self.comboBox_2.setItemText(2, _translate("label_platform", "Playstation", None))
        self.comboBox_2.setItemText(3, _translate("label_platform", "Nintendo", None))
        self.comboBox_2.setItemText(4, _translate("label_platform", "Xbox", None))
        self.comboBox_3.setItemText(1, _translate("label_platform", "Action", None))
        self.comboBox_3.setItemText(2, _translate("label_platform", "Adventure", None))
        self.comboBox_3.setItemText(3, _translate("label_platform", "Sports", None))
        self.comboBox_3.setItemText(4, _translate("label_platform", "Strategy", None))
        self.comboBox_3.setItemText(5, _translate("label_platform", "Racing", None))
        self.comboBox_3.setItemText(6, _translate("label_platform", "Simulation", None))
        self.comboBox_3.setItemText(7, _translate("label_platform", "Others", None))

import xz_rc

if __name__ == "__main__":
    import sys
    os.remove("genre.txt")
    os.remove("platform.txt")
    f= open("genre.txt","w+")
    f= open("platform.txt","w+")
    app = QtGui.QApplication(sys.argv)
    label_platform = QtGui.QDialog()
    ui = Ui_label_platform()
    ui.setupUi(label_platform)
    label_platform.show()
    sys.exit(app.exec_())

