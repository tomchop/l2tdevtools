# -*- coding: utf-8 -*-
"""Helper for building projects from source."""

from __future__ import unicode_literals

import os


class BuildHelper(object):
  """Helper to build projects from source."""

  LOG_FILENAME = 'build.log'

  def __init__(self, project_definition, l2tdevtools_path):
    """Initializes a build helper.

    Args:
      project_definition (ProjectDefinition): project definition.
      l2tdevtools_path (str): path to the l2tdevtools directory.
    """
    super(BuildHelper, self).__init__()
    self._data_path = os.path.join(l2tdevtools_path, 'data')
    self._project_definition = project_definition

  def _IsPython2Only(self):
    """Determines if the project only supports Python version 2.

    Returns:
      bool: True if the project only support Python version 2.
    """
    return 'python2_only' in self._project_definition.build_options

  def _IsPython3Only(self):
    """Determines if the project only supports Python version 3.

    Returns:
      bool: True if the project only support Python version 3.
    """
    return 'python3_only' in self._project_definition.build_options

  def CheckBuildDependencies(self):
    """Checks if the build dependencies are met.

    Returns:
      list[str]: build dependency names that are not met or an empty list.
    """
    build_dependencies = self._project_definition.build_dependencies
    if not build_dependencies:
      build_dependencies = []
    return list(build_dependencies)

  # pylint: disable=unused-argument
  def CheckBuildRequired(self, source_helper_object):
    """Checks if a build is required.

    Args:
      source_helper_object (SourceHelper): source helper.

    Returns:
      bool: True if a build is required, False otherwise.
    """
    return True

  def CheckProjectConfiguration(self):
    """Checks if the project configuration is correct.

    Returns:
      bool: True if the project configuration is correct, False otherwise.
    """
    return True
