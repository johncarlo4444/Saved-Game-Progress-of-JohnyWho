	for i in range(get_world_size()):
		for j in range(get_world_size()):
			#do a flip on every tile
			if can_harvest():
				harvest()
				move(North)
				plant(Entities.Bush)
			move(East)
	