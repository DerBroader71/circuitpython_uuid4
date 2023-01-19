Introduction
============

This is a CircuitPython library to generate a UUID version 4.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.

Usage Example
=============

```python

    import circuitpython_uuid4 as Uuid
    uuid = Uuid.generate_uuid_v4()
    print(uuid)
```
