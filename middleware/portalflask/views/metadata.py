from flask import Blueprint, current_app, abort
import os
import markdown
import re
import urllib2



portal_metadata = Blueprint('metadata', __name__)


get_key =  re.compile('/*/*([\w+\s+\w+]+):/*/*')
pre_re = '/*/*{var}:/*/*.*?\\n(\\n)?'

@portal_metadata.route('/metadata/<metadata_type>/<path:metadata_id>', methods=["get"])
def metadata(metadata_type, metadata_id):

   metadata_id = urllib2.unquote(metadata_id).replace('/','_')
   html = getHTML(metadata_type,metadata_id)
   if (html != "error"):
      return html
   else:
      abort(404)


def mergeAllTheThings():
   pass
      

def getText(metadata_type,metadata_id):
   print metadata_id
   metadata_id = metadata_id.lower()
   if (metadata_type in current_app.config.get('MARKDOWN_DIRS')):
      markdown_dir = current_app.config.get('MARKDOWN_ROOT')
      type_dir = '%s/%s' % (markdown_dir, metadata_type)
      types = { x.lower(): x for x in os.listdir(type_dir)}
      temp_type = '%s.md' % metadata_id
      if temp_type in types:
         type_name = types[temp_type]
         with open('%s/%s' % (type_dir, type_name)) as tfile:
            text = tfile.read()
            return text
         return "error"
   return "error"

def getHTML(metadata_type,metadata_id):
   metadata_id = metadata_id.lower()
   if (metadata_type in current_app.config.get('MARKDOWN_DIRS')):
      markdown_dir = current_app.config.get('MARKDOWN_ROOT')
      type_dir = '%s/%s' % (markdown_dir, metadata_type)
      types = { x.lower(): x for x in os.listdir(type_dir)}
      temp_type = '%s.md' % metadata_id
      if temp_type in types:
         type_name = types[temp_type]
         with open('%s/%s' % (type_dir, type_name)) as tfile:
            text = tfile.read()
            current_app.logger.debug(text)
            html = markdown.markdown(text).replace('\n','')
            return html
         return "error"
   return "error"


def getDict(list_of_markdown):
   outdict = {}
   for a in list_of_markdown:
      if (len(get_key.findall(a)) > 0):
         outdict[get_key.findall(a)[0]] = a
   return outdict