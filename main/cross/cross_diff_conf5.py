#!/usr/bin/env python
# -*- coding: utf-8 -*-

#@author  Bin Hong

import sys,os
local_path = os.path.dirname(__file__)
root = os.path.join(local_path, '..')
sys.path.append(root)

import model.model_param_set as param_set


ta =  param_set.d_dir_ta

l_params = [
        ("ta1_GBCv1n1000md3_l1_s2000e2009" , ta["ta1"], "label1", ("2010-01-01", '2015-12-31'),  0.0),
        ("ta1_GBCv1n1000md3_l2_s2000e2009" , ta["ta1"], "label2", ("2010-01-01", '2015-12-31'),  0.0),
        ("ta1_GBCv1n1000md3_l3_s2000e2009" , ta["ta1"], "label3", ("2010-01-01", '2015-12-31'),  0.0),
        ("ta1_GBCv1n1000md3_l4_s2000e2009" , ta["ta1"], "label4", ("2010-01-01", '2015-12-31'),  0.0),
        ("ta1_GBCv1n1000md3_l5_s2000e2009" , ta["ta1"], "label5", ("2010-01-01", '2015-12-31'),  0.0),
        ("ta1_GBCv1n1000md3_l6_s2000e2009" , ta["ta1"], "label6", ("2010-01-01", '2015-12-31'),  0.0),
        ("ta1_GBCv1n1000md3_l8_s2000e2009" , ta["ta1"], "label8", ("2010-01-01", '2015-12-31'),  0.0),
        ("ta1_GBCv1n1000md3_l10_s2000e2009", ta["ta1"], "label10", ("2010-01-01", '2015-12-31'), 0.0),
        ("ta1_GBCv1n1000md3_l15_s2000e2009", ta["ta1"], "label15", ("2010-01-01", '2015-12-31'), 0.0),
        ("ta1_GBCv1n1000md3_l20_s2000e2009", ta["ta1"], "label20", ("2010-01-01", '2015-12-31'), 0.0),

        ("ta1_GBCv1n1000md3_l1_s2000e2009" , ta["ta1"], "label1", ("2010-01-01", '2015-12-31'),  0.6),
        ("ta1_GBCv1n1000md3_l2_s2000e2009" , ta["ta1"], "label2", ("2010-01-01", '2015-12-31'),  0.6),
        ("ta1_GBCv1n1000md3_l3_s2000e2009" , ta["ta1"], "label3", ("2010-01-01", '2015-12-31'),  0.6),
        ("ta1_GBCv1n1000md3_l4_s2000e2009" , ta["ta1"], "label4", ("2010-01-01", '2015-12-31'),  0.6),
        ("ta1_GBCv1n1000md3_l5_s2000e2009" , ta["ta1"], "label5", ("2010-01-01", '2015-12-31'),  0.6),
        ("ta1_GBCv1n1000md3_l6_s2000e2009" , ta["ta1"], "label6", ("2010-01-01", '2015-12-31'),  0.6),
        ("ta1_GBCv1n1000md3_l8_s2000e2009" , ta["ta1"], "label8", ("2010-01-01", '2015-12-31'),  0.6),
        ("ta1_GBCv1n1000md3_l10_s2000e2009", ta["ta1"], "label10", ("2010-01-01", '2015-12-31'), 0.6),
        ("ta1_GBCv1n1000md3_l15_s2000e2009", ta["ta1"], "label15", ("2010-01-01", '2015-12-31'), 0.6),
        ("ta1_GBCv1n1000md3_l20_s2000e2009", ta["ta1"], "label20", ("2010-01-01", '2015-12-31'), 0.6),

        ("ta1_GBCv1n1000md3_l1_s2000e2009" , ta["ta1"], "label1", ("2010-01-01", '2015-12-31'),  0.7),
        ("ta1_GBCv1n1000md3_l2_s2000e2009" , ta["ta1"], "label2", ("2010-01-01", '2015-12-31'),  0.7),
        ("ta1_GBCv1n1000md3_l3_s2000e2009" , ta["ta1"], "label3", ("2010-01-01", '2015-12-31'),  0.7),
        ("ta1_GBCv1n1000md3_l4_s2000e2009" , ta["ta1"], "label4", ("2010-01-01", '2015-12-31'),  0.7),
        ("ta1_GBCv1n1000md3_l5_s2000e2009" , ta["ta1"], "label5", ("2010-01-01", '2015-12-31'),  0.7),
        ("ta1_GBCv1n1000md3_l6_s2000e2009" , ta["ta1"], "label6", ("2010-01-01", '2015-12-31'),  0.7),
        ("ta1_GBCv1n1000md3_l8_s2000e2009" , ta["ta1"], "label8", ("2010-01-01", '2015-12-31'),  0.7),
        ("ta1_GBCv1n1000md3_l10_s2000e2009", ta["ta1"], "label10", ("2010-01-01", '2015-12-31'), 0.7),
        ("ta1_GBCv1n1000md3_l15_s2000e2009", ta["ta1"], "label15", ("2010-01-01", '2015-12-31'), 0.7),
        ("ta1_GBCv1n1000md3_l20_s2000e2009", ta["ta1"], "label20", ("2010-01-01", '2015-12-31'), 0.7),

        ("ta1_GBCv1n1000md3_l1_s2000e2009" , ta["ta1"], "label1", ("2010-01-01", '2015-12-31'),  0.8),
        ("ta1_GBCv1n1000md3_l2_s2000e2009" , ta["ta1"], "label2", ("2010-01-01", '2015-12-31'),  0.8),
        ("ta1_GBCv1n1000md3_l3_s2000e2009" , ta["ta1"], "label3", ("2010-01-01", '2015-12-31'),  0.8),
        ("ta1_GBCv1n1000md3_l4_s2000e2009" , ta["ta1"], "label4", ("2010-01-01", '2015-12-31'),  0.8),
        ("ta1_GBCv1n1000md3_l5_s2000e2009" , ta["ta1"], "label5", ("2010-01-01", '2015-12-31'),  0.8),
        ("ta1_GBCv1n1000md3_l6_s2000e2009" , ta["ta1"], "label6", ("2010-01-01", '2015-12-31'),  0.8),
        ("ta1_GBCv1n1000md3_l8_s2000e2009" , ta["ta1"], "label8", ("2010-01-01", '2015-12-31'),  0.8),
        ("ta1_GBCv1n1000md3_l10_s2000e2009", ta["ta1"], "label10", ("2010-01-01", '2015-12-31'), 0.8),
        ("ta1_GBCv1n1000md3_l15_s2000e2009", ta["ta1"], "label15", ("2010-01-01", '2015-12-31'), 0.8),
        ("ta1_GBCv1n1000md3_l20_s2000e2009", ta["ta1"], "label20", ("2010-01-01", '2015-12-31'), 0.8),
        ]

