import sched


scheduler = sched.scheduler()

def hello():
  print("Olá Pessoal")
  scheduler.enter(delay=(3), priority=0, action=hello)

hello()

scheduler.run(blocking=True)
