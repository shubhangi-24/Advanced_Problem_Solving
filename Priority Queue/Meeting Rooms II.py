
	def minimum_rooms(meetings):

		meetings.sort(key = lambda x : x[0])
		min_heap = []

		for meeting in meetings:
			if len(min_heap) > 0 and meeting[0] >= min_heap[0]:
				heappop(min_heap)
			heappush(min_heap, meeting[1])

		return len(min_heap)
