roster = ['Anna Barbara', 'Catherine Do', 'Eric Frederick',
          'Gabriel Hernandez', 'Ivy Joo', 'Kelly Marks']
for name in roster :
    splitname = name.split ()
    formattedname =  ' {2:10} {1:10} -----{0:>10}' .format (splitname[0], splitname[1], 'hello')
    print(formattedname)

