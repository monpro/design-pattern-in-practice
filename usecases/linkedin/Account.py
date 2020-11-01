from usecases.linkedin.const import AccountStatus


class Account:
  def __init__(self, id, password, status=AccountStatus.ACTIVE):
    self.id = id
    self.password = password
    self.status = status

  def reset_password(self):
    pass

