#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2019 The hyperspy_cl developers
#
# This file is part of hyperspy_cl.
#
# hyperspy_cl is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# hyperspy_cl is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with hyperspy_cl.  If not, see <http://www.gnu.org/licenses/>.


def push_metadata_through(dummy, *args, **kwargs):
    """
    This function pushes loaded metadata through to hyperspy_cl objects, it is to be used for one
    purpose, see the __init__ of ElectronDiffraction2D for an example.

    Parameters
    ----------
    dummy :
        This will always be the "self" of the object to be initialised

    args : list
        This will always be the "args" of the object to be initialised

    kwargs : dict
        This will always be the "args" of the object to be initialised

    Returns
    -------
    dummy,args,kwargs :
        The input variables, adjusted correctly
    """
    try:
        meta_dict = args[0].metadata.as_dictionary()
        kwargs.update({'metadata': meta_dict})
    except AttributeError:
        pass  # this is because a numpy array has been passed
    except IndexError:
        pass  # this means that map continues to work.

    return dummy, args, kwargs
