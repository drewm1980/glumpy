#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2013, Nicolas P. Rougier. All rights reserved.
# Distributed under the terms of the new BSD License.
# -----------------------------------------------------------------------------
import unittest
import numpy as np
from collection import Collection

vtype = [('position', 'f4', 2)]
utype = [('color',    'f4', 3)]
itype = np.uint32

vertices = np.zeros(4, dtype=vtype)
indices  = np.array([0,1,2,0,2,3], dtype=itype)
uniforms = np.ones(1,dtype=utype)


class CollectionDefault(unittest.TestCase):


    def test_init(self):
        C = Collection(vtype,utype)
        assert len(C) == 0

    def test_append_one_item(self):
        C = Collection(vtype, utype)
        C.append(vertices, indices, uniforms)
        C.append(vertices, indices, uniforms)
        assert len(C) == 2
        assert np.allclose( C[0].indices , indices )
        assert np.allclose( C[1].indices , 4+indices )

    def test_append_several_item_1(self):
        C = Collection(vtype, utype)
        C.append(np.zeros(40, dtype=vtype), indices, uniforms, itemsize=4)
        for i in xrange(10):
            assert np.allclose(C[i].indices, 4*i+indices)

    def test_append_several_item_2(self):
        C = Collection(vtype, utype)
        C.append(np.zeros(40, dtype=vtype),
                 np.zeros(10, dtype=itype), itemsize=(4,1))
        for i in xrange(10):
            assert np.allclose(C[i].indices, 4*i)

    def test_insert_one_item(self):
        C = Collection(vtype, utype)
        C.append(vertices, indices, uniforms)
        C.insert(0, vertices, indices, uniforms)
        assert len(C) == 2
        assert np.allclose(C[0].indices , indices)
        assert np.allclose(C[1].indices , 4+indices)

    def test_delete_one_item(self):
        C = Collection(vtype, utype)
        C.append(vertices, indices, uniforms)
        C.append(vertices, indices, uniforms)
        del C[0]
        assert np.allclose(C[0].indices , indices)

    def test_delete_several_item(self):
        C = Collection(vtype, utype)
        C.append(np.zeros(40, dtype=vtype), indices, uniforms, itemsize=4)
        del C[:9]
        assert np.allclose(C[0].indices , indices)


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    unittest.main()

