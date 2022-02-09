# Conclusion: A<B<C<D.....<Z<a<b....<z

veggie =  input ('State a vegetable: ' )
if veggie > 'spinach':
    print (' this word starts with t, u, v, w, x, y, z' )
elif veggie > 'carrot':
    print (' greater than carrot and less than spinach' )
elif veggie > 'broccoli':
    print (' greater than broccoli and less than carrot' )
elif veggie > 'Zoo':
    print (' capital word' )
elif veggie > 'Jade':
    print (' capital word and larger thhan Jade' )
elif veggie > 'ABC':
    print (' ABC' )
else:
    print (' GG')