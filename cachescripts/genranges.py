#!/usr/bin/env python

import sys
import csv
import json
from argparse import ArgumentParser
from pprint import pprint
import urllib2
from contextlib import contextmanager

# context manager to allow the use of a url in the 'with x as y' python syntax
# I.E. it just has to yield and have a finally to allow auto closing
@contextmanager
def urlopener(inURL):
    """Open a URL and yield the fileHandle then close the connection when leaving the 'with' clause."""
    fileHandle = urllib2.urlopen(inURL)
    try:     yield fileHandle
    finally: fileHandle.close()

def format_tag(data, entry):
   if entry == 'Indicator name':
      tag = data[entry]
      #tag = data[entry].lower()
   else:
      tag = data[entry][0].capitalize()+data[entry][1:]
      
   return tag

#END_DEF


cmdParser = ArgumentParser()
cmdParser.add_argument("-p", "--providers", action="store", dest="providers_file_name", 
                       help="Providers config file", required=True)
cmdParser.add_argument("-f", "--file", action="store", dest="file_name", 
                       help="Load table from specified file")
cmdParser.add_argument("-u", "--url", action="store", dest="sheet_url", help="URL for a google docs csv for input")
cmdParser.add_argument("-v", "--verbose", action="store_true", dest="verbose", help="Enable verbose output")
cmdParser.add_argument("-t", "--tags", action="store_true", dest="show_tags", help="Enable tags output")
cmdParser.add_argument("-r", "--ranges", action="store_true", dest="show_ranges", help="Enable ranges output")
opts = cmdParser.parse_args()


# block to test if we have either a file or a URL as argparse doesnt have mutual inclusion
#print "testing inputs"
#print opts.sheet_url
#print opts.file_name
if opts.sheet_url is None and opts.file_name is None:
   cmdParser.error("either an input file (-f) or a URL to a google doc (-u) ae required")

# The tag data files are held as CSV with headers.
# E.g.
# ,,,,,,,,"MSFD Descriptors",,,,
# "NetCDF variable","Description","Provider","Indicator name","Interval","Provider mask","Region","Type","Eutrophication","Biodiversity","Foodwebs","Hydrography","Fisheries"
# "Cod__adult_","cod adult","Cefas","Adult Cod","daily","P","N. Atlantic","Fish",,,"Foodwebs",,"Fisheries"
# "Herbivorous_and_Omnivorous_zooplankton__copepods_","Herbivorous_and_Omnivorous_zooplankton__copepods_","Cefas","Zooplankton","daily","P","N. Atlantic","Zooplankton","Eutrophocation","Biodiversity","Foodwebs",,
# "Herring__adult_","herring adult","Cefas","Adult herring","daily","P","N. Atlantic","Fish",,,"Foodwebs",,"Fisheries"
# "Herring__juvenile_0__1_","herring juvenile","Cefas","Juvenile herring","daily","P","N. Atlantic","Fish",,,"Foodwebs",,"Fisheries"
# "Juvenile_Cod_0_2__0_40cm_","juvenile cod","Cefas","Juvenile cod","daily","P","N. Atlantic","Fish",,,"Foodwebs",,"Fisheries"
# "Phytoplankton","phytoplankton  ","Cefas","Phytoplankton biomass","daily","P","N. Atlantic","Phytoplankton","Eutrophocation","Biodiversity","Foodwebs",,
# "Plaice","plaice","Cefas","Plaice","daily","P","N. Atlantic","Fish",,,"Foodwebs",,"Fisheries"
# "Sandeels","sandeels","Cefas","Sandeels","daily","P","N. Atlantic","Fish",,,"Foodwebs",,"Fisheries"

tags = {}
ranges = {}

with open(opts.providers_file_name, 'rb') as providers:
   tags = json.load(providers)

#print(json.dumps(tags, sort_keys=True, indent=4))
indicators = {}

# switch between either the url for a google docs sheet or a filepath for a csv file
if opts.sheet_url is not None:
   file_handler = urlopener(opts.sheet_url)
else:
   file_handler = open(opts.file_name, 'rb')



with file_handler as csvfile:
   # Tell the CSV reader to ignore leading whitespace.
   reader = csv.reader(csvfile, delimiter=',', quotechar='"', skipinitialspace=True)

   # Skip first line
   reader.next()

   line2 = [l.strip() for l in reader.next()]

   # Now add all the rows
   for row in reader:
      # Turn it into a dict
      data = dict(zip(line2, [l.strip() for l in row]))

      # Skip unless the row is flagged as in the portal
      if (data['Portal'] != 'Yes'):
         continue

      # We have 3 different ways in which the netCDF files (and TDS services) are arranged.
      # It can be just one file which we can name by provider
      # or it might be divided into different files for different time intervals so we have
      # to append the interval onto the name as we use a different TDS rule to create it.
      # Finally, each variable might be in a separate file so append the variable name.
      if (data['Provider mask'] == 'P'):
         provider_id = data['Provider'].lower()
      elif (data['Provider mask'] == 'P_I'):
         provider_id = data['Provider'].lower() + '_' + data['Interval'].lower()
      elif (data['Provider mask'] == 'P_V'):
         provider_id = data['Provider'].lower() + '_' + data['NetCDF variable']

      if (opts.verbose):
         print >>sys.stderr, provider_id, data['NetCDF variable']
         #print >>sys.stderr, data

      # Process the columns which can generate tags
      for entry, category in {'Indicator name': 'niceName', 'Region': 'region', 'Type': 'Ecosystem_Element', 'Interval': 'interval', 'Expert Judgement': 'Confidence', 'Model Used': 'model', 'Contact': 'contact'}.iteritems():

         # If the higher level layer structure has not been created yet (first time we got here)
         # then create what is needed and retry.
         if data[entry] != '':
            try:
               tags[provider_id]['indicators'][data['NetCDF variable']][category]=format_tag(data, entry)
            except KeyError as detail:
               if tags[provider_id].has_key('indicators'):
                  tags[provider_id]['indicators'][data['NetCDF variable']]={}
               else:
                  tags[provider_id]['indicators']={}
                  tags[provider_id]['indicators'][data['NetCDF variable']]={}

               tags[provider_id]['indicators'][data['NetCDF variable']][category]=format_tag(data, entry)
            #endtry
      #endfor

      # We have a special format for the MSFD descriptors in the table. Each descriptor has 
      # its own column
      for entry in ['Eutrophication','Biological Diversity','Foodwebs','Hydrographical Conditions','Commercial Fisheries']:   
         if (data[entry] != ''):  
            try:
               tags[provider_id]['indicators'][data['NetCDF variable']]['MSFD'].append(format_tag(data, entry))
            except KeyError as detail:
               tags[provider_id]['indicators'][data['NetCDF variable']]['MSFD']=[]
               tags[provider_id]['indicators'][data['NetCDF variable']]['MSFD'].append(format_tag(data, entry))

      # Process the range columns
      provider_id = data['Provider'].upper()
      for entry in {'Min', 'Max'}:
         if data[entry] == '':
            continue

         # If the higher level layer structure has not been created yet (first time we got here)
         # then create what is needed and retry.
         try:
            ranges[provider_id][data['NetCDF variable']][entry]=data[entry]
         except KeyError as detail:
            if ranges.has_key(provider_id):
               ranges[provider_id][data['NetCDF variable']]={}
            else:
               ranges[provider_id]={}
               ranges[provider_id][data['NetCDF variable']]={}

            ranges[provider_id][data['NetCDF variable']][entry]=data[entry]
      #endfor

#endwith

if opts.show_tags:
   if (opts.verbose):
      print >>sys.stderr, "Printing tags"
   layers = []
   for t in tags:
      if (opts.verbose): print >>sys.stderr, "Tag %s" % t
      layers.append(tags[t])

   tag_list = 'layers = %s' % json.dumps(layers, sort_keys=True, indent=4)
   print(tag_list)
#   pprint(tags)
#endif
   
if opts.show_ranges:
   range_list = 'ranges = %s' % json.dumps(ranges, sort_keys=True, indent=4)
   #print(range_list)
   if (opts.verbose):
      print >>sys.stderr, "Printing ranges"

   for layer_name, layer in ranges.iteritems():
      print '<datasetPath pathSpec="%s*">' % layer_name
      print '   <pathDefaults>'
      print '      <defaultPaletteName>nasa_rainbow</defaultPaletteName>'
      print '      <logScaling>false</logScaling>'
      print '   </pathDefaults>'
      print '   <variables>'
      for variable_name, variable in layer.iteritems():
         print '      <variable id="%s">' % variable_name
         print '         <defaultColorScaleRange>%f %f</defaultColorScaleRange>' % (float(variable['Min']), float(variable['Max']))
         print '      </variable>'
      #endfor

      print '   </variables>'
      print '</datasetPath>'
#endif
