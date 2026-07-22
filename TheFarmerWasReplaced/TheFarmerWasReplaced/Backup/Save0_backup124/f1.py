while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			#Harvest on every tile
			if can_harvest():
				plant(Entities.Grass)
				harvest()
				plant(Entities.Bush)
				harvest()
				move(North)	
		move(East)