import random
# Potential Alien Values
aln_key = ['color', 'points', 'xpos', 'ypos', 'speed', 'status']
aln_color = ['red', 'green', 'yellow']
aln_point = [5, 10, 15]
aln_speed = ['slow', 'medium', 'fast']
aln_sttus = ['alive', 'dead']

# Example Alien Dictionaries
alien11 = {'color': 'red', 'points': 5, 'xpos': 0, 'ypos': 0, 'speed': 'slow', 'status': "alive"}
alien12 = {'color': 'red', 'points': 5, 'xpos': 25, 'ypos': 0, 'speed': 'slow', 'status': "alive"}
alien13 = {'color': 'red', 'points': 5, 'xpos': 50, 'ypos': 0, 'speed': 'slow', 'status': "alive"}
alien21 = {'color': 'yellow', 'points': 10, 'xpos': 0, 'ypos': 50, 'speed': 'slow', 'status': "alive"}
alien12 = {'color': 'yellow', 'points': 10, 'xpos': 25, 'ypos': 50, 'speed': 'slow', 'status': "alive"}
alien23 = {'color': 'yellow', 'points': 15, 'xpos': 50, 'ypos': 50, 'speed': 'slow', 'status': "alive"}
alien31 = {'color': 'green', 'points': 15, 'xpos': 0, 'ypos': 75, 'speed': 'slow', 'status': "alive"}
alien32 = {'color': 'green', 'points': 15, 'xpos': 25, 'ypos': 75, 'speed': 'slow', 'status': "alive"}
alien33 = {'color': 'green', 'points': 15, 'xpos': 50, 'ypos': 75, 'speed': 'slow', 'status': "alive"}




# Determine how far to move the alien based on its current speed.
def GetMoveDistance(alien):
	if alien11['speed'] == 'slow':
		x_increment = 1
	elif alien11['speed'] == 'medium':
		x_increment = 2
	else:
		x_increment = 3
	return x_increment

# The new position is the old position plus the increment.
def GetNewPosition(alien, increment):
	alien['xpos'] = alien['xpos'] + increment
	print(f"New position: {alien['xpos']}")


if __name__ == '__main__':

	aln_hordes = []
	# Generate 30 aliens
	for aln_number in range(30):
		aln_newaln = {'color': 'red', 'points': 5, 'xpos': 0, 'ypos': 0, 'speed': 'slow', 'status': "alive"}
		aln_hordes.append(aln_newaln)
	print(f"Number of Aliens created: {len(aln_hordes)}")

	# Modify First Three Aliens
	for alien in aln_hordes[:3]:
		if alien['color'] == 'green':
			alien['color'] = 'yellow'
			alien['speed'] = 'medium'
			alien['points'] = 10
		elif alien['color'] == 'yellow':
			alien['color'] = 'red'
			alien['speed'] = 'fast'
			alien['points'] = 15
