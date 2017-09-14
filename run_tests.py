#!/usr/bin/env python

# Common command to run from terminal
# python -m unittest discover -s ./ -p "*_test.py"

import unittest

if __name__ == "__main__":
    suite = unittest.TestLoader().discover('.', pattern = "*_test.py")
    unittest.TextTestRunner(verbosity=0).run(suite)