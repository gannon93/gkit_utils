"""
    Author: Zachary Gannon
    Module: config_reader.py
"""

from __future__ import absolute_import, division, print_function

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser


class ConfigReader():
    """Summary
        Wrapper for Python's ConfigParser module.

        See link for ini file configuration:
            https://wiki.python.org/moin/ConfigParserExamples
    Attributes:
        cparser (ConfigParser): class scoped ConfigParser object
    """
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        self.cparser = ConfigParser()

    def read_config(self, filepath):
        """Summary
            Method reads and returns the contents of an ini file.
        Args:
            filepath (String): file path to ini file

        Returns:
            Dictionary: mapping of keys and values of specified ini file
        """
        return self.cparser.read(filepath)

    def get_sections(self):
        """Summary
            Method returns list of section headings in ini file
        Returns:
            List: mapping of section headings in specified ini file
        """
        return self.cparser.sections()

    def read_section_map(self, section):
        """Summary
            Method returns dictionary of contents under the specified
            section heading.
        Args:
            section (Stirng): name of section to read contents of

        Returns:
            Dictionary: mapping of keys and values for the specified section
        """
        return_dict = {}
        options = self.cparser.options(section)
        for option in options:
            try:
                return_dict[option] = self.cparser.get(section, option)
                if return_dict[option] == -1:
                    print("skip: %s" % option)
            except Exception as e:
                print("exception on %s!" % option)
                return_dict[option] = None
        return return_dict
