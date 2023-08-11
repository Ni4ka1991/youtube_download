#!/usr/bin/env python3
from pytube import YouTube

link = input( "Enter the link here >>>  " )

yt = YouTube( link )

#Show details
#print( "Title:", yt.title )

#Getting the higest resolution 
ys = yt.streams.get_highest_resolution()

#Starting download
print( "Download ..." )

ys.download()
print( "Download complited!" )
