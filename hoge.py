# -*- coding: utf-8 -*-

# assert 文をシンプルに書ける ok_ eq_ メソッドの読み込み
from nose.tools import ok_, eq_

# テストケース
# test で始まる名前の関数で書けばOK
def test_1_is_true():
    ok_(bool(1))

def test_1_plus_2():
    eq_(1 + 2, 3)


