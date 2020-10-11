import asyncio
import time
from asyncio import Future
from threading import current_thread

shutdown = False


async def resolver(future):
  print("loop running in resolver thread {0} = {1} ?".format(current_thread().getName(),
                                                   asyncio.get_event_loop().is_running()))

  await asyncio.sleep(10)
  future.set_result(None)


async def monitor_core():
  global shutdown

  while not shutdown:
    print("Alive at {0}".format(time.time()))
    await asyncio.sleep(1)


async def core():
  global shutdown

  print("running core")
  future = Future()
  monitor_core_future = asyncio.ensure_future(monitor_core())
  resolver_future = asyncio.ensure_future(resolver(future))

  print("loop running in core thread {0} = {1} ?".format(current_thread().getName(),
                                                   asyncio.get_event_loop().is_running()))
  await future
  await asyncio.sleep(2)
  shutdown = True
  await monitor_core_future, resolver_future


if __name__ == "__main__":

  loop = asyncio.get_event_loop()
  print("loop running in thread {0} = {1} ?".format(current_thread().getName(),
                                                   asyncio.get_event_loop().is_running()))
  loop.run_until_complete(core())
  print("main exiting")