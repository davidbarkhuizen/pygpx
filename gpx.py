from operator import itemgetter, attrgetter, methodcaller

class GPX(object):

	def __init__(self, metadata, tracks, waypoints):

		self.metadata = metadata
		self.tracks = tracks
		self.waypoints = waypoints

	def get_locations_at_time(self, time):

		locations = []

		track_points = []

		# aggregate
		#
		for track in self.tracks:
			for track_segment in track.segments:
				track_points.extend(track_segment.points)

		# sort by time
		track_points = sorted(track_points, key=attrgetter('time'))

		before = []
		at = []
		after = []

		for p in track_points:

			if p.time < time:
				before.append(p)
			elif p.time == time:
				at.append(p)
			else:
				after.append(p)

		if len(at) > 0:
			return at
		else:
			locations = []
			if len(before) > 0:
				immediately_before = before[-1]
				locations.append(immediately_before)
			if len(after) > 0:
				immediately_after = after[0]
				locations.append(immediately_after)
			return locations