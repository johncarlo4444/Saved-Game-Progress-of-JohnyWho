while True:
	if can_harvest():
		harvest()
		move(North)
		plant(Entities.Bush)
	else:
		move(North)

		