from intermine.webservice import Service

new_run = 'yes'
flymine = Service('www.flymine.org/query', token = '01n6a26f47fe1f32G7c2')
for imlist in flymine.get_all_lists():
  print imlist.name
  if imlist.name.startswith('nova_'):
    new_run = 'no'

print ('==================')

import glob

path = '/micklem/data/thalemine/wdir/ws/*.dat'
files = glob.glob(path)
for index, name in enumerate(files): # 'file' is a builtin type
  print index, name
  if new_run == 'yes':
    new_list = flymine.create_list(name, "Gene", 'nova_' + str(index))


print ('==================+++++')

for imlist in flymine.get_all_lists():
  if imlist.name.startswith('nova_'):
    print imlist.name
    i = 0
    for item in imlist.calculate_enrichment('pathway_enrichment'):
      if item.p_value > 0.01:
        print item.identifier, item.description, item.p_value
        if i == 0:
          new_list = flymine.create_list(item.identifier, "Pathway", "rich_pathways")
          i += 1
        else:
          new_list.append(item.identifier)
