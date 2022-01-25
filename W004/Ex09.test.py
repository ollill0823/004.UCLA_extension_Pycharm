## 12 character spaces for first name   (left aligned because string)
## 12 character spaces for last name    (left aligned because string)
## 3 character spaces for age           (right aligned because int)
## 12 character spaces for occupation   (left aligned because string)
roster = [['Anna','Barbara',35,'nurse'],
              ['Catherine','Do',45,'physicist'],
              ['Eric','Frederick',28,'teacher'],
              ['Gabriel','Hernandez',55,'surgeon'],
              ['Ivy','Joo',31,'engineer'],
              ['Kelly','Marks',21,'student']]

for person in roster:       ## First loop through, person will be ['Anna','Barbara',35,'nurse']
    formattedtext = '{:12}{:12}{:3}{:12}'.format(person[0], person[1], person[2], person[3])
    print(formattedtext)
