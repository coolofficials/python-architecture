# pyright: reportUnusedVariable=false
# pyright: reportGeneralTypeIssues=false
# flake8: noqa

import datetime

import pytest

import model

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
later = tomorrow + datetime.timedelta(days=10)


def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch = model.Batch("batch_1", "SMALL-TABLE", 20, eta=today)
    order_line = model.OrderLine("order_1", "SMALL-TABLE", 2)

    batch.allocate(order_line)

    assert batch.available_quantity == 18


def test_can_allocate_if_available_greater_than_required():
    large_batch = model.Batch("batch_1", "SMALL-TABLE", 20, eta=today)
    small_order_line = model.OrderLine("order_1", "SMALL-TABLE", 2)

    assert large_batch.can_allocate(small_order_line)


def test_cannot_allocate_if_available_smaller_than_required():
    small_batch = model.Batch("batch_1", "SMALL-TABLE", 2, eta=today)
    large_order_line = model.OrderLine("order_1", "SMALL-TABLE", 5)

    assert small_batch.can_allocate(large_order_line) is False


def test_can_allocate_if_available_equal_to_required():
    batch = model.Batch("batch_1", "SMALL-TABLE", 2, eta=today)
    order_line = model.OrderLine("order_1", "SMALL-TABLE", 2)

    assert batch.can_allocate(order_line)


def test_cannot_allocate_if_skus_do_not_match():
    small_table_batch = model.Batch("batch_1", "SMALL-TABLE", 2, eta=today)
    large_table_order_line = model.OrderLine("order_1", "LARGE-TABLE", 2)

    assert small_table_batch.can_allocate(large_table_order_line) is False


def test_prefers_warehouse_batches_to_shipments():
    pytest.fail("todo")


def test_prefers_earlier_batches():
    pytest.fail("todo")
