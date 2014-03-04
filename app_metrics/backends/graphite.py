# coding=utf-8

from app_metrics.tasks import graphite_metric_task


def _get_func(async):
    return graphite_metric_task.delay if async else graphite_metric_task


def metric(slug, num=1, async=True, **kwargs):
    _get_func(async)(slug, num, **kwargs)


