
class Publisher:
	def __init__(self):
		self.subscribers = []
	def add_subscriber(self, subscriber):
		self.subscribers.append(subscriber)
	def remove_subscriber(self, subscriber):
		self.subscribers.remove(subscriber)
	def notify(self, event):
		print(len(self.subscribers))
		for subscriber in self.subscribers:
			subscriber.handle(event)
