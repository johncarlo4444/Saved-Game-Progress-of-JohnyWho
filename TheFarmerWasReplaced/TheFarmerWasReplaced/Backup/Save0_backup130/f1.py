while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			#Harvest on every tile
			if can_harvest():
				harvest()
				plant(Entities.Bush)
				move(North)	
				if can_harvest():
					harvest()
					plant(Entities.Grass)
					move(North)
		move(East)