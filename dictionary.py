alien_0 = {'color': 'green', 'point': 5}
print(alien_0['color'])
new_points = alien_0['point']
print("you just earned" + " "+ str(new_points) + " " + "points")
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0['color'] = 'yellow'
print("color is now" + " " + alien_0['color'])
alien_0['speed'] = 'fast'
print(alien_0)
print("original x_position: " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3
else:
    x_increment = 4
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("new x_position: " + str(alien_0['x_position']))

