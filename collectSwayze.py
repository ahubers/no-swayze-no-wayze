#!/usr/bin/env python
from SwayzeBaby import SwayzeBaby
from corner import Corner 


swayze = SwayzeBaby()
corner = Corner()
# swaykeys = [" Skatetown, U.S.A.", "The Outsiders","Uncommon Valor","Grandview, U.S.A. ","Red Dawn ","Youngblood ","Dirty Dancing ","Steel Dawn ","Tiger Warsaw ","Road House ","Next of Kin ","Ghost ","Point Break ","City of Joy ","Father Hood ","Tall Tale ","To Wong Foo Thanks for Everything, Julie Newmar ","Three Wishes ","Black Dog ","Letters from a Killer ","Forever Lulu ","Green Dragon ","Donnie Darko ","Waking Up in Reno ","One Last Dance ","11:14 ","Dirty Dancing: Havana Nights ","Keeping Mum ","The Fox and the Hound 2 ","Jump! ","Christmas in Wonderland ","Powder Blue "]
swaykeys = [""]
for keyword in swaykeys:
	query = "swayze " + keyword
	results = swayze.fetchAllSwayze(query)
	for key, value in results.iteritems():
		url = key
		title = value
		query = "INSERT INTO swayze (url, title, fake) VALUES ('{0}', '{1}', {2})".format(url, title, 0)
		corner.query(query)


		# row = SwayzeDB(url=key, title=value)
		# row.save()
	
	# 	for result in data:
	# 		#Make a new instance of our db wrapper.

	# 		corner.query(query)

	# 		id = corner.lastInsert()
	# 		colors = self.getColorScheme(url)

	# 		for (color in colors):
	# 			query = "INSERT INTO colors (swayze_id, color, frequency, fake) VALUES ({0}, '{1}', {2}, {3})".format(lastId, color, 0.0, 0)
	# 			corner.query(query)
				

