class Message:
  def __init__(self, sent_to, message_body, media):
    self.__sent_to = sent_to
    self.__message_body = message_body
    self.__media = media